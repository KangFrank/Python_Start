#-*-: utf-8 
#Made by Mr. Kang, just for reference
import pandas as pd
import os
import matplotlib.pyplot as plt

#save figure and data in specific path
data_path = './video_games_sales1.csv'
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    df_data = pd.read_csv(data_path)
    return df_data



def process_data(df_data):
    #去除缺失值
    df_data['NewYear']=0
    year=[]
    for i in range(len(df_data['Year'])):
        if str(df_data.iloc[i]['Year']).split()[0]=='2':
            df_data.iloc[i]['NewYear']=int(df_data.iloc[i]['Year'])
    print(df_data['Year'])
    df_data['Year'].to_csv(os.path.join(output_path,'year.csv'))

"""
    cond = (df_data['Year'] >= 2005) & (df_data['Year'] <= 2017)
    cln_df_data1 = cln_df_data[cond]
    filtered_data = cln_df_data1.copy()

    #加总global_sales
    filtered_data['Global_sales'] = filtered_data['NA_Sales'] + filtered_data['EU_Sales'] +filtered_data['JP_Sales'] +filtered_data['Other_Sales']

    #将销售额小于<5M的厂商过滤掉
    filtered_df_data = filtered_data[filtered_data['Global_sales'] > 5]

    #print("原数据有{}行,处理后的数据有:{}行".format(df_data.shape[0],filtered_data.shape[0]))
    return filtered_df_data
"""
def analyze_data(filtered_df_data):
    # 全球销量的top20的游戏

    top20_games_sales = filtered_df_data.sort_values(by = 'Global_sales',ascending = False).head(20)

    producer_games_com_sales = filtered_df_data.groupby('Publisher')[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum()
    #print(top20_games_sales)
    # print('----------')
    # print(producer_games_com_sales)
    return top20_games_sales,producer_games_com_sales


def save_and_show_results(top20_games_sales,producer_games_com_sales):
    top20_games_sales.to_csv(os.path.join(output_path,'top20_sale.csv'),index = False)
    producer_games_com_sales.to_csv(os.path.join(output_path,'global_sales.csv'))


    top20_games_sales.plot(kind = 'bar',x='Name',y='Global_sales')
    plt.title('top20 sales')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'top20_sales.png'))
    plt.show()

    producer_games_com_sales.plot.bar(stacked = True)
    plt.title('Games Sales Comparison (2005-2017)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'Game_sale_comparison.png'))
    plt.show()



def main():
    #收集数据
    df_data = collect_data()

    #数据处理
    filtered_df_data = process_data(df_data)

    #分析数据
    #top20_games_sales,producer_games_com_sales = analyze_data(filtered_df_data)


    #数据保存与可视化
    #save_and_show_results(top20_games_sales,producer_games_com_sales)


if __name__ == '__main__':
    main()