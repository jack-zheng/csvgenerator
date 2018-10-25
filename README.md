# csvgenerator
### Aim
Phase I: python script to generate csv file  
Phase II: desktop app(UI) to generate csv file

#### Phase I Log
给出一个 csv  文件作为模板， 传入数量， 生成对应的文件来做 perf 测试的数据源  
e.g. csv file demo  

| id | fname | lname | col4 |
| ------ | ------ | ------ | ----- |
| perf | pfname | plname | col4value |

input: 3  
output:

| id | fname | lname | col4 |
| ------ | ------ | ------ | ----- |
| perf1 | pfname1 | plname1 | col4value |
| perf2 | pfname2 | plname2 | col4value |
| perf3 | pfname3 | plname3 | col4value |

使用 csv lib 完成工作 

update OCT-25 ------------------  
接口变动: 提供了一个生成默认文件的方法  
generate_general_csv(sample_file, increment_count)  

参数:  
sample_file, 你想要 copy 的文件，确保该文件再当前文件夹下  
increment_count, 你想要生成的数据的条数