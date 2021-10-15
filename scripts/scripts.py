import os

validation_schema = {
    'status': 'valid',
    'ol_error': [
        {
            'sample_name': 'sample_name',
            'marker': []
        }
    ],
    'merge_error': [
        {
            'sample_name': 'sample_name',
            'marker': []
        }
    ],
    'gender_error': [],
    'low_homozygote_height': []
}

project_schema = {
    'project_name': 'filename',
    'samples': [
        {
            'sample_name': 'sample_name',
            'markers': [
                {
                    'marker_name': 'marker',
                    'alleles': [],
                    'alleles_high': []
                }
            ]
        }
    ]
}

ALLELE_COUNT = 6
REQUIRED_KEYS = ('Sample Name',
                 'Marker',
                 'Allele 1',
                 'Allele 2',
                 'Allele 3',
                 'Allele 4',
                 'Allele 5',
                 'Allele 6')

Y_LOCUS = ('Yindel', 'DYS391', 'DYS576', 'DYS570', 'DYS389I', 'DYS635', 'DYS389II',
           'DYS627', 'DYS460', 'DYS458', 'DYS19', 'YGATAH4', 'DYS448', 'DYS456',
           'DYS390', 'DYS438', 'DYS392', 'DYS518', 'DYS437', 'DYS385', 'DYS449',
           'DYS393', 'DYS439', 'DYS481', 'DYF387S1', 'DYS533')


def merge(old_alleles, new_alleles):
    merge_validate = True
    if len(set(old_alleles)) == 1:
        return new_alleles, merge_validate
    elif old_alleles != new_alleles and len(set(new_alleles)) > 1:
        merge_validate = False
    return old_alleles, merge_validate


def index_item(array, item, key):
    return next((i for i, x in enumerate(array) if x[key] == item), None)


def ol_validator(alleles):
    return False if 'OL' in alleles else True


def get_alleles(row, header):
    return [row[header.get(f'Allele {i + 1}')] if f'Allele {i + 1}' in header else '' for i in range(ALLELE_COUNT)]


def get_dict(header):
    return {key: index for index, key in enumerate(header) if key in REQUIRED_KEYS}


def form_result(status, ol_error, merge_error, gender_error, low_homozygote_height, project):
    return {
        'status': status,
        'ol_error': ol_error,
        'merge_error': merge_error,
        'gender_error': gender_error,
        'low_homozygote_height': low_homozygote_height,
        'project': project
    }


def line_to_array(line):
    return line.split('\t')


def validate_fields(header):
    for i in REQUIRED_KEYS[:4]:
        if i not in header:
            return 'invalid'


def export_table_parser(file):
    status = 'valid'
    ol_error = []
    merge_error = []
    gender_error = []
    low_homozygote_height = []
    project = {'samples': []}

    with open(file, 'r') as file:
        data = file
        project['project_name'] = os.path.basename(file.name)
        keys_line, *rest = data.read().splitlines()
    header = line_to_array(keys_line)
    if validate_fields(header) == 'invalid':
        status = 'invalid'
        return form_result(
            status,
            ol_error,
            merge_error,
            gender_error,
            low_homozygote_height,
            project
        )
    header = get_dict(header)
    for row in rest:
        merge_validate = True
        row = line_to_array(row)
        sample_name = row[header['Sample Name']]
        marker = 'Amelogenin' if row[header['Marker']] == 'AMEL' else row[header['Marker']]
        alleles = get_alleles(row, header)
        ol_validate = ol_validator(alleles)

        sample_index = index_item(project['samples'], sample_name, 'sample_name')
        if sample_index is None:
            project['samples'].append(
                {
                    'sample_name': sample_name,
                    'markers': [
                        {
                            'marker_name': marker,
                            'alleles': alleles
                        }
                    ]
                }
            )
        else:
            marker_index = index_item(project['samples'][sample_index]['markers'], marker, 'marker_name')
            if marker_index is None:
                project['samples'][sample_index]['markers'].append(
                    {
                        'marker_name': marker,
                        'alleles': alleles
                    }
                )
            else:
                old_alleles = project['samples'][sample_index]['markers'][marker_index]['alleles']
                alleles, merge_validate = merge(old_alleles, alleles)
                project['samples'][sample_index]['markers'][marker_index]['alleles'] = alleles

        # валидация
        if not ol_validate:
            status = 'partial_valid'
            index = index_item(ol_error, sample_name, 'sample_name')
            if index is None:
                ol_error.append(
                    {
                        'sample_name': sample_name,
                        'marker': [marker]
                    }
                )
            else:
                ol_error[index]['marker'].append(marker)

        if not merge_validate:
            status = 'partial_valid'
            index = index_item(merge_error, sample_name, 'sample_name')
            if index is None:
                merge_error.append(
                    {
                        'sample_name': sample_name,
                        'marker': [marker]
                    }
                )
            else:
                merge_error[index]['marker'].append(marker)

    for sample in project['samples']:
        sample_name = sample['sample_name']
        amelogenin_in_sample = False
        gender = 'female'
        for marker in sample['markers']:
            if marker['marker_name'] == 'Amelogenin':
                amelogenin_in_sample = True
            if amelogenin_in_sample and 'Y' in marker['alleles']:
                gender = 'male'
        for marker in sample['markers']:
            if amelogenin_in_sample and gender == 'female' and marker['marker_name'] in Y_LOCUS and len(
                    set(marker['alleles'])) > 1:
                status = 'partial_valid'
                if sample_name not in gender_error:
                    gender_error.append(sample_name)

    return form_result(
        status,
        ol_error,
        merge_error,
        gender_error,
        low_homozygote_height,
        project
    )

def form_error(array, key):
    result = ''
    text = {
        'ol_error': 'содержится неименнованная аллель',
        'merge_error': 'прозошла ошибка слияния'
    }
    for item in array[key]:
        if item:
            result += 'В объекте {} в локус{} {} {};\n'.format(
                    item['sample_name'],
                    'e' if len(item['marker']) == 1 else 'ах',
                    text[key],
                    ', '.join(item['marker'])
                )
    return result


def create_report(data):
    ol_result = form_error(data, 'ol_error')
    merge_result = form_error(data, 'merge_error')
    gender_result = ''

    for item in data['gender_error']:
        if item:
            gender_template = 'В объекте {} возможна ошибка определения пола;\n'.format(
                item
            )
            gender_result += gender_template

    report = {
        'valid': 'Ошибок не обнаружено',
        'invalid': 'Загруженный файл не корректен, убедитесь в наличии всех необходимых полей',
        'partial_valid': f'{ol_result}{merge_result}{gender_result}'
    }

    return report[data['status']]
