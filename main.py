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
    df_first = pd.DataFrame()
    grouped = df.groupby('사용기관명')
    for group in grouped:
        print(group)
        # df_first = pd.concat([df_first,group])
    # print(df_first)

def main():
    # set_data()
    get_data()


if __name__=='__main__':
    main()