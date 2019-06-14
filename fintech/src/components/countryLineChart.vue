<template>
    <div>
        <div style="text-align: center">
            <el-select v-model="selectCountry" placeholder="請選擇國家" @change="changeCountry">
                <el-option
                        v-for="item in optionCountry"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
            <el-select v-model="selectFund" placeholder="請選擇基金" @change="changeFund">
                <el-option
                        v-for="item in optionFund"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
        </div>
        基金價格與各項指標
        <ve-line :data="chartData" :extand="extend"></ve-line>
        各項指標相關係數
        <el-table
                :data="tableData"
                style="width: 100%"
                height="auto">
            <el-table-column
                    fixed
                    prop="fundName"
                    label="基金名稱"
                    width="auto">
            </el-table-column>
            <el-table-column
                    prop="fundValuePeople"
                    label="基金價格與定期定額投資人數"
                    width="auto">
            </el-table-column>
            <el-table-column
                    prop="newsPeople"
                    label="新聞事件與定期定額投資人數"
                    width="auto">
            </el-table-column>
            <el-table-column
                    prop="newsFundValue"
                    label="新聞事件與基金價格"
                    width="auto">
            </el-table-column>
            <el-table-column
                    prop="newsLeadFundValue"
                    label="新聞事件一個月後與基金價格"
                    width="auto">
            </el-table-column>
            <el-table-column
                    prop="newsLeadPeople"
                    label="新聞事件一個月後與定期定額扣款人數"
                    width="auto">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
    import { addMonths, getYear, getMonth } from 'date-fns';

    export default {
        name: "countryLineChart",
        data: function () {
            return {
                selectCountry: 'china',
                selectFund: '',
                chartData: {
                    columns: [],
                    rows: []
                },
                optionCountry: [{
                    value: 'china',
                    label: '中國'
                }, {
                    value: 'russia',
                    label: '俄羅斯'
                }, {
                    value: 'india',
                    label: '印度'
                }, {
                    value: 'brazil',
                    label: '巴西'
                }],
                optionFund: [],
                chinaFundNameList: [],
                chinaFundValueList: [],
                chinaIndexNameList: [],
                chinaIndexValueList: [],
                chinaPeopleValueList: [],
                chinaEmoValueList: [],
                chinaFundValuePeopleList: [],
                chinaNewsPeopleList: [],
                chinaNewsFundValueList: [],
                chinaNewsLeadFundValueList: [],
                chinaNewsLeadPeopleList: [],
                russiaFundNameList: [],
                russiaFundValueList: [],
                russiaIndexNameList: [],
                russiaIndexValueList: [],
                russiaEmoValueList: [],
                russiaPeopleValueList: [],
                russiaFundValuePeopleList: [],
                russiaNewsPeopleList: [],
                russiaNewsFundValueList: [],
                russiaNewsLeadFundValueList: [],
                russiaNewsLeadPeopleList: [],
                indiaFundNameList: [],
                indiaFundValueList: [],
                indiaIndexNameList: [],
                indiaIndexValueList: [],
                indiaEmoValueList: [],
                indiaPeopleValueList: [],
                indiaFundValuePeopleList: [],
                indiaNewsPeopleList: [],
                indiaNewsFundValueList: [],
                indiaNewsLeadFundValueList: [],
                indiaNewsLeadPeopleList: [],
                brazilFundNameList: [],
                brazilFundValueList: [],
                brazilIndexNameList: [],
                brazilIndexValueList: [],
                brazilEmoValueList: [],
                brazilPeopleValueList: [],
                brazilFundValuePeopleList: [],
                brazilNewsPeopleList: [],
                brazilNewsFundValueList: [],
                brazilNewsLeadFundValueList: [],
                brazilNewsLeadPeopleList: [],
                extend: {
                    legend: {
                        bottom: 0,
                        type: 'scroll'
                    }
                },
                tableData: []
            }
        },
        mounted() {
            let json = require('../assets/json/china_percentage.json');
            for(let name in json) {
                this.chinaFundNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.chinaFundValueList.push(fundValueTempList);
            }
            json = require('../assets/json/china_index.json');
            for(let name in json) {
                this.chinaIndexNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.chinaIndexValueList.push(fundValueTempList);
            }
            json = require('../assets/json/china_emo.json');
            for(let index  in json) {
                this.chinaEmoValueList.push(json[index]);
            }
            json = require('../assets/json/china_people.json');
            for(let name in json) {
                let peopleValueTempList = [];
                for(let people in json[name]) {
                    peopleValueTempList.push(json[name][people]);
                }
                this.chinaPeopleValueList.push(peopleValueTempList);
            }
            json = require('../assets/json/china_corr.json');
            for(let index in this.chinaFundNameList) {
                for(let key in json) {
                    if(this.chinaFundNameList[index] === key) {
                        for(let temp in json[key]){
                            if(temp === 'money_people') {
                                this.chinaFundValuePeopleList.push(json[key][temp]);
                            } else if(temp === 'news_people') {
                                this.chinaNewsPeopleList.push(json[key][temp]);
                            } else if(temp === 'news_money') {
                                this.chinaNewsFundValueList.push(json[key][temp]);
                            } else if(temp === 'news_lead_money') {
                                this.chinaNewsLeadFundValueList.push(json[key][temp]);
                            } else if(temp === 'news_lead_people') {
                                this.chinaNewsLeadPeopleList.push(json[key][temp]);
                            }
                        }
                    }
                }
            }
            json = require('../assets/json/russia_percentage.json');
            for(let name in json) {
                this.russiaFundNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.russiaFundValueList.push(fundValueTempList);
            }
            json = require('../assets/json/russia_index.json');
            for(let name in json) {
                this.russiaIndexNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.russiaIndexValueList.push(fundValueTempList);
            }
            json = require('../assets/json/russia_emo.json');
            for(let index  in json) {
                this.russiaEmoValueList.push(json[index]);
            }
            json = require('../assets/json/russia_people.json');
            for(let name in json) {
                let peopleValueTempList = [];
                for(let people in json[name]) {
                    peopleValueTempList.push(json[name][people]);
                }
                this.russiaPeopleValueList.push(peopleValueTempList);
            }
            json = require('../assets/json/russia_corr.json');
            for(let index in this.russiaFundNameList) {
                for(let key in json) {
                    if(this.russiaFundNameList[index] === key) {
                        for(let temp in json[key]){
                            if(temp === 'money_people') {
                                this.russiaFundValuePeopleList.push(json[key][temp]);
                            } else if(temp === 'news_people') {
                                this.russiaNewsPeopleList.push(json[key][temp]);
                            } else if(temp === 'news_money') {
                                this.russiaNewsFundValueList.push(json[key][temp]);
                            } else if(temp === 'news_lead_money') {
                                this.russiaNewsLeadFundValueList.push(json[key][temp]);
                            } else if(temp === 'news_lead_people') {
                                this.russiaNewsLeadPeopleList.push(json[key][temp]);
                            }
                        }
                    }
                }
            }
            json = require('../assets/json/india_percentage.json');
            for(let name in json) {
                this.indiaFundNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.indiaFundValueList.push(fundValueTempList);
            }
            json = require('../assets/json/india_index.json');
            for(let name in json) {
                this.indiaIndexNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.indiaIndexValueList.push(fundValueTempList);
            }
            json = require('../assets/json/india_emo.json');
            for(let index  in json) {
                this.indiaEmoValueList.push(json[index]);
            }
            json = require('../assets/json/india_people.json');
            for(let name in json) {
                let peopleValueTempList = [];
                for(let people in json[name]) {
                    peopleValueTempList.push(json[name][people]);
                }
                this.indiaPeopleValueList.push(peopleValueTempList);
            }
            json = require('../assets/json/india_corr.json');
            for(let index in this.indiaFundNameList) {
                for(let key in json) {
                    if(this.indiaFundNameList[index] === key) {
                        for(let temp in json[key]){
                            if(temp === 'money_people') {
                                this.indiaFundValuePeopleList.push(json[key][temp]);
                            } else if(temp === 'news_people') {
                                this.indiaNewsPeopleList.push(json[key][temp]);
                            } else if(temp === 'news_money') {
                                this.indiaNewsFundValueList.push(json[key][temp]);
                            } else if(temp === 'news_lead_money') {
                                this.indiaNewsLeadFundValueList.push(json[key][temp]);
                            } else if(temp === 'news_lead_people') {
                                this.indiaNewsLeadPeopleList.push(json[key][temp]);
                            }
                        }
                    }
                }
            }
            json = require('../assets/json/brazil_percentage.json');
            for(let name in json) {
                this.brazilFundNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.brazilFundValueList.push(fundValueTempList);
            }
            json = require('../assets/json/brazil_index.json');
            for(let name in json) {
                this.brazilIndexNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.brazilIndexValueList.push(fundValueTempList);
            }
            json = require('../assets/json/brazil_emo.json');
            for(let index  in json) {
                this.brazilEmoValueList.push(json[index]);
            }
            json = require('../assets/json/brazil_people.json');
            for(let name in json) {
                let peopleValueTempList = [];
                for(let people in json[name]) {
                    peopleValueTempList.push(json[name][people]);
                }
                this.brazilPeopleValueList.push(peopleValueTempList);
            }
            json = require('../assets/json/brazil_corr.json');
            for(let index in this.brazilFundNameList) {
                for(let key in json) {
                    if(this.brazilFundNameList[index] === key) {
                        for(let temp in json[key]){
                            if(temp === 'money_people') {
                                this.brazilFundValuePeopleList.push(json[key][temp]);
                            } else if(temp === 'news_people') {
                                this.brazilNewsPeopleList.push(json[key][temp]);
                            } else if(temp === 'news_money') {
                                this.brazilNewsFundValueList.push(json[key][temp]);
                            } else if(temp === 'news_lead_money') {
                                this.brazilNewsLeadFundValueList.push(json[key][temp]);
                            } else if(temp === 'news_lead_people') {
                                this.brazilNewsLeadPeopleList.push(json[key][temp]);
                            }
                        }
                    }
                }
            }
            this.changeCountry();
        },
        methods: {
            changeCountry() {
                this.optionFund = [];
                this.selectFund = '';
                if(this.selectCountry === 'china') {
                    for(let index in this.chinaFundNameList) {
                        let option = {};
                        option.value = index.toString();
                        option.label = this.chinaFundNameList[index];
                        this.optionFund.push(option);
                    }
                } else if(this.selectCountry === 'russia') {
                    for(let index in this.russiaFundNameList) {
                        let option = {};
                        option.value = index.toString();
                        option.label = this.russiaFundNameList[index];
                        this.optionFund.push(option);
                    }
                } else if(this.selectCountry === 'india') {
                    for(let index in this.indiaFundNameList) {
                        let option = {};
                        option.value = index.toString();
                        option.label = this.indiaFundNameList[index];
                        this.optionFund.push(option);
                    }
                } else if(this.selectCountry === 'brazil') {
                    for(let index in this.brazilFundNameList) {
                        let option = {};
                        option.value = index.toString();
                        option.label = this.brazilFundNameList[index];
                        this.optionFund.push(option);
                    }
                }
            },
            changeFund() {
                this.chartData.columns = ['日期'];
                this.chartData.rows = [];
                this.tableData = [];
                if(this.selectCountry === 'china') {
                    for(let name of this.chinaIndexNameList)
                        this.chartData.columns.push(name);
                    this.chartData.columns.push(this.chinaFundNameList[parseInt(this.selectFund)]);
                    this.chartData.columns.push('新聞事件');
                    this.chartData.columns.push('定期定額扣款人數');
                    let date = new Date(2016, 3);
                    for(let index in this.chinaEmoValueList) {
                        date = addMonths(date, 1);
                        let row = {
                            '日期': getYear(date).toString()+'/'+getMonth(date).toString()
                        };
                        for(let i in this.chinaIndexValueList) {
                            row[this.chartData.columns[parseInt(i)+1]] = this.chinaIndexValueList[parseInt(i)][index];
                        }
                        row[this.chinaFundNameList[parseInt(this.selectFund)]] = this.chinaFundValueList[parseInt(this.selectFund)][index];
                        row['新聞事件'] = (this.chinaEmoValueList[index]/100);
                        row['定期定額扣款人數'] = this.chinaPeopleValueList[parseInt(this.selectFund)][index];
                        // console.log(row);
                        this.chartData.rows.push(row);
                    }
                    let tableDataObject = {};
                    tableDataObject.fundName = this.chinaFundNameList[parseInt(this.selectFund)];
                    tableDataObject.fundValuePeople = this.chinaFundValuePeopleList[parseInt(this.selectFund)];
                    tableDataObject.newsFundValue = this.chinaNewsFundValueList[parseInt(this.selectFund)];
                    tableDataObject.newsPeople = this.chinaNewsPeopleList[parseInt(this.selectFund)];
                    tableDataObject.newsLeadFundValue = this.chinaNewsLeadFundValueList[parseInt(this.selectFund)];
                    tableDataObject.newsLeadPeople = this.chinaNewsLeadPeopleList[parseInt(this.selectFund)];
                    this.tableData.push(tableDataObject);
                } else if(this.selectCountry === 'russia') {
                    for(let name of this.russiaIndexNameList)
                        this.chartData.columns.push(name);
                    this.chartData.columns.push(this.russiaFundNameList[parseInt(this.selectFund)]);
                    this.chartData.columns.push('新聞事件');
                    this.chartData.columns.push('定期定額扣款人數');
                    let date = new Date(2016, 3);
                    for(let index in this.russiaEmoValueList) {
                        date = addMonths(date, 1);
                        let row = {
                            '日期': getYear(date).toString()+'/'+getMonth(date).toString()
                        };
                        for(let i in this.russiaIndexValueList) {
                            row[this.chartData.columns[parseInt(i)+1]] = this.russiaIndexValueList[parseInt(i)][index];
                        }
                        row[this.russiaFundNameList[parseInt(this.selectFund)]] = this.russiaFundValueList[parseInt(this.selectFund)][index];
                        row['新聞事件'] = (this.russiaEmoValueList[index]/100);
                        row['定期定額扣款人數'] = this.russiaPeopleValueList[parseInt(this.selectFund)][index];
                        this.chartData.rows.push(row);
                    }
                    let tableDataObject = {};
                    tableDataObject.fundName = this.russiaFundNameList[parseInt(this.selectFund)];
                    tableDataObject.fundValuePeople = this.russiaFundValuePeopleList[parseInt(this.selectFund)];
                    tableDataObject.newsFundValue = this.russiaNewsFundValueList[parseInt(this.selectFund)];
                    tableDataObject.newsPeople = this.russiaNewsPeopleList[parseInt(this.selectFund)];
                    tableDataObject.newsLeadFundValue = this.russiaNewsLeadFundValueList[parseInt(this.selectFund)];
                    tableDataObject.newsLeadPeople = this.russiaNewsLeadPeopleList[parseInt(this.selectFund)];
                    this.tableData.push(tableDataObject);
                } else if(this.selectCountry === 'india') {
                    for(let name of this.indiaIndexNameList)
                        this.chartData.columns.push(name);
                    this.chartData.columns.push(this.indiaFundNameList[parseInt(this.selectFund)]);
                    this.chartData.columns.push('新聞事件');
                    this.chartData.columns.push('定期定額扣款人數');
                    let date = new Date(2016, 3);
                    for(let index in this.indiaEmoValueList) {
                        date = addMonths(date, 1);
                        let row = {
                            '日期': getYear(date).toString()+'/'+getMonth(date).toString()
                        };
                        for(let i in this.indiaIndexValueList) {
                            row[this.chartData.columns[parseInt(i)+1]] = this.indiaIndexValueList[parseInt(i)][index];
                        }
                        row[this.indiaFundNameList[parseInt(this.selectFund)]] = this.indiaFundValueList[parseInt(this.selectFund)][index];
                        row['新聞事件'] = (this.indiaEmoValueList[index]/100);
                        row['定期定額扣款人數'] = this.indiaPeopleValueList[parseInt(this.selectFund)][index];
                        // console.log(row);
                        this.chartData.rows.push(row);
                    }
                    let tableDataObject = {};
                    tableDataObject.fundName = this.indiaFundNameList[parseInt(this.selectFund)];
                    tableDataObject.fundValuePeople = this.indiaFundValuePeopleList[parseInt(this.selectFund)];
                    tableDataObject.newsFundValue = this.indiaNewsFundValueList[parseInt(this.selectFund)];
                    tableDataObject.newsPeople = this.indiaNewsPeopleList[parseInt(this.selectFund)];
                    tableDataObject.newsLeadFundValue = this.indiaNewsLeadFundValueList[parseInt(this.selectFund)];
                    tableDataObject.newsLeadPeople = this.indiaNewsLeadPeopleList[parseInt(this.selectFund)];
                    this.tableData.push(tableDataObject);
                } else if(this.selectCountry === 'brazil') {
                    for(let name of this.brazilIndexNameList)
                        this.chartData.columns.push(name);
                    this.chartData.columns.push(this.brazilFundNameList[parseInt(this.selectFund)]);
                    this.chartData.columns.push('新聞事件');
                    this.chartData.columns.push('定期定額扣款人數');
                    let date = new Date(2016, 3);
                    for(let index in this.brazilEmoValueList) {
                        date = addMonths(date, 1);
                        let row = {
                            '日期': getYear(date).toString()+'/'+getMonth(date).toString()
                        };
                        for(let i in this.brazilIndexValueList) {
                            row[this.chartData.columns[parseInt(i)+1]] = this.brazilIndexValueList[parseInt(i)][index];
                        }
                        row[this.brazilFundNameList[parseInt(this.selectFund)]] = this.brazilFundValueList[parseInt(this.selectFund)][index];
                        row['新聞事件'] = (this.brazilEmoValueList[index]/100);
                        row['定期定額扣款人數'] = this.brazilPeopleValueList[parseInt(this.selectFund)][index];
                        // console.log(row);
                        this.chartData.rows.push(row);
                    }
                    let tableDataObject = {};
                    tableDataObject.fundName = this.brazilFundNameList[parseInt(this.selectFund)];
                    tableDataObject.fundValuePeople = this.brazilFundValuePeopleList[parseInt(this.selectFund)];
                    tableDataObject.newsFundValue = this.brazilNewsFundValueList[parseInt(this.selectFund)];
                    tableDataObject.newsPeople = this.brazilNewsPeopleList[parseInt(this.selectFund)];
                    tableDataObject.newsLeadFundValue = this.brazilNewsLeadFundValueList[parseInt(this.selectFund)];
                    tableDataObject.newsLeadPeople = this.brazilNewsLeadPeopleList[parseInt(this.selectFund)];
                    this.tableData.push(tableDataObject);
                }
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>