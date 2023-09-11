def get_pillar_code(goal_id):
    if 'ENV' in goal_id:
        return 'ENV'
    if 'ECO' in goal_id:
        return 'ECO'
    if 'SOC' in goal_id:
        return 'SOC'
    return ''

def alter_meta(meta, context):
    # Auto-calculate settings based on the indicator id.
    indicator_id = context['indicator_id']
    indicator_id_parts = indicator_id.split('-')
    first_part = indicator_id_parts[0]
    is_in_framework = first_part.startswith('ENV') or first_part.startswith('ECO') or first_part.startswith('SOC')
    if len(indicator_id_parts) == 3 and is_in_framework:

        # These are used by Open SDG.
        meta['indicator_number'] = indicator_id
        meta['goal_number'] = indicator_id_parts[0]
        meta['goal_name'] = 'global_goals.' + meta['goal_number'] + '-title'
        meta['target_number'] = indicator_id_parts[0] + '-' + indicator_id_parts[1]
        meta['target_name'] = 'global_targets.' + meta['target_number'] + '-title'
        meta['indicator_name'] = 'indicators.' + indicator_id + '-title'

        # These are used in the Vanuatu national metadata tab.
        national_meta = {
            'PillarCode': get_pillar_code(meta['goal_number']),
            'PillarDescription': 'pillars.' + get_pillar_code(meta['goal_number']),
            'GoalId': meta['goal_number'],
            'GoalDescription': meta['goal_name'],
            'PolicyObjectiveId': meta['target_number'],
            'PolicyObjectiveDescription': meta['target_name'],
            'IndicatorId': indicator_id,
            'IndicatorDescription': meta['indicator_name'],
        }
        # Use these national defaults if nothing is set.
        for key in national_meta:
            if key not in meta or meta[key] == '' or meta[key] is None:
                meta[key] = national_meta[key]

    meta['national_geographical_coverage'] = 'Vanuatu'
    return meta
