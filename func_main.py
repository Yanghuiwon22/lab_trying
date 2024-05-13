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

def group_area():
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
    return group_area

def second_data():
    df = pd.read_csv('./output/output_first.csv')
    df = df.drop(['캠퍼스구분','순번','건축물코드','건축물명','층구분','층코드','층번호','호실코드'], axis=1)
    return df



def main():
    # area_sum()
    pass


if __name__=='__main__':
    main()