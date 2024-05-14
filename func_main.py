import os
import pandas as pd



def set_data():
    input_dir = './input'
    output_dir = './output'

    df = pd.DataFrame()

    filelist = os.listdir(input_dir)
    for i in filelist:
        raw_data = pd.DataFrame(pd.read_excel(f'{input_dir}/{i}'))
        df = pd.concat([df, raw_data])
        df.reset_index(drop=True, inplace=True)

    df.to_csv(f'{output_dir}/output.csv', index=False)

def get_data():
    df = pd.read_csv('./output/output.csv')
    df_first = pd.DataFrame([])

    grouped = df.groupby('사용기관명')
    group_nm = []
    group_area = []

    for group_name, group_df in grouped:
        df_first = pd.concat([df_first,group_df])

        group_nm.append(group_name)
        group_area.append(group_df['전용면적'].sum())
    df_first.reset_index(drop=True, inplace=True)


    df_first.to_csv('./output/output_first.csv', index=False)
    group_nm.insert(0,'전체')
    return group_nm

def group_area(csv_output):
    # df = pd.read_csv('./output/output.csv')
    df_first = pd.DataFrame([])

    grouped = csv_output.groupby('사용기관명')
    group_nm = []
    group_area = []

    for group_name, group_df in grouped:
        df_first = pd.concat([df_first,group_df])

        group_nm.append(group_name)
        group_area.append(group_df['전용면적'].sum())
    df_first.reset_index(drop=True, inplace=True)


    # df_first.to_csv('./output/output_first.csv', index=False)
    group_nm.insert(0,'전체')
    return [group_nm, group_area]

def second_data():
    df = pd.read_csv('./output/output_first.csv')
    df = df.drop(['캠퍼스구분','순번','건축물코드','건축물명','층구분','층코드','층번호','호실코드'], axis=1)
    return df

def division_area():
    df = pd.read_csv('./output/output.csv')

    df_department = pd.DataFrame()
    df_bisiness = pd.DataFrame()

    group_nm = get_data()[1:]
    for i in group_nm:
        if '학과' in i or '학부' in i or '대학원' in i:
            df_department = pd.concat([df_department, df[df['사용기관명'] == i][['사용기관명','전용면적']]])

        else:
            df_bisiness = pd.concat([df_bisiness, df[df['사용기관명'] == i][['사용기관명','전용면적']]])

    df_department.reset_index(drop=True, inplace=True)
    df_bisiness.reset_index(drop=True, inplace=True)

    print(df_department )
    df_department.to_csv('./output/output_department.csv', index=False)
    df_bisiness.to_csv('./output/output_bisiness.csv', index=False)

    return df_department, df_bisiness

def main():
    division_area()
    # pass


if __name__=='__main__':
    main()