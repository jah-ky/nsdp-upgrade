import pandas as pd
import yaml

def get_indicator_slug(text):
    text = text.replace(' ', '')
    text = text.replace('.', '-')
    return text


filepath = 'scripts/NSDP_INDICATORS_METADATA.xlsx'
meta_excel = pd.ExcelFile(filepath)
meta_df = meta_excel.parse(meta_excel.sheet_names[0], index_col=0, squeeze=True)
meta_df = meta_df.fillna('')
meta_df = meta_df.rename(columns={
    'Pillar Code': 'PillarCode',
    'Pillar Description': 'PillarDescription',
    'Goal Id': 'GoalId',
    'Goal Description': 'GoalDescription',
    'Policy Objective id': 'PolicyObjectiveId',
    'Policy Objective Description': 'PolicyObjectiveDescription',
    'Indicator id': 'IndicatorId',
    'Indicator description': 'IndicatorDescription',
    'Target': 'TargetDescription',
    'SDG Alignment1': 'SDGAlignment1',
    'SDG Alignment2': 'SDGAlignment2',
    'SDG Alignment3': 'SDGAlignment3',
    'SDG Alignment4': 'SDGAlignment4',
    'SDG Alignment5': 'SDGAlignment5',
    'Computation Method': 'ComputationMethod',
    'Computation Unit': 'ComputationUnit',
    'Data Source': 'DataSource',
    'Frequency of Collection': 'FrequencyOfCollection',
})

for index, row in meta_df.iterrows():
    slug = get_indicator_slug(row['IndicatorId'])
    meta_path = 'meta/' + slug + '.yml'
    with open(meta_path, 'r') as stream:
        meta = yaml.load(stream, Loader=yaml.FullLoader)
    for key, value in row.iteritems():
        meta[key] = row[key]
    meta['SDGAlignment'] = meta['SDGAlignment1']
    if meta['SDGAlignment2'] != '':
        meta['SDGAlignment'] += ', ' + meta['SDGAlignment2']
    if meta['SDGAlignment3'] != '':
        meta['SDGAlignment'] += ', ' + meta['SDGAlignment3']
    if meta['SDGAlignment4'] != '':
        meta['SDGAlignment'] += ', ' + meta['SDGAlignment4']
    if meta['SDGAlignment5'] != '':
        meta['SDGAlignment'] += ', ' + meta['SDGAlignment5']
    del meta['SDGAlignment1']
    del meta['SDGAlignment2']
    del meta['SDGAlignment3']
    del meta['SDGAlignment4']
    del meta['SDGAlignment5']
    with open(meta_path, 'w') as stream:
        yaml.dump(meta, stream)
