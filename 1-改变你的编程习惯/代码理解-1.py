def rfm_user(df):
    if df['M_score'] == 1 and df['R_score'] == 1 and df['F_score'] == 1:
        return '重要价值用户'
    if df['M_score'] == 1 and df['R_score'] == 1 and df['F_score'] == 0:
        return '重要发展用户'
    if df['M_score'] == 1 and df['R_score'] == 0 and df['F_score'] == 1:
        return '重要保持用户'
    if df['M_score'] == 1 and df['R_score'] == 0 and df['F_score'] == 0:
        return '重要挽留用户'
    if df['M_score'] == 0 and df['R_score'] == 1 and df['F_score'] == 1:
        return '一般价值用户'
    if df['M_score'] == 0 and df['R_score'] == 1 and df['F_score'] == 0:
        return '一般发展用户'
    if df['M_score'] == 0 and df['R_score'] == 0 and df['F_score'] == 1:
        return '一般保持用户'
    if df['M_score'] == 0 and df['R_score'] == 0 and df['F_score'] == 0:
        return '一般挽留用户'
