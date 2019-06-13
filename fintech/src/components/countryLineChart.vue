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
                chinaEmoValueList: [],
                russiaFundNameList: [],
                russiaFundValueList: [],
                russiaIndexNameList: [],
                russiaIndexValueList: [],
                russiaEmoValueList: [],
                indiaFundNameList: [],
                indiaFundValueList: [],
                indiaIndexNameList: [],
                indiaIndexValueList: [],
                indiaEmoValueList: [],
                brazilFundNameList: [],
                brazilFundValueList: [],
                brazilIndexNameList: [],
                brazilIndexValueList: [],
                brazilEmoValueList: [],
                extend: {
                    legend: {
                        bottom: 0,
                        type: 'scroll'
                    }
                }
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
                if(this.selectCountry === 'china') {
                    for(let name of this.chinaIndexNameList)
                        this.chartData.columns.push(name);
                    this.chartData.columns.push(this.chinaFundNameList[parseInt(this.selectFund)]);
                    this.chartData.columns.push('新聞事件');
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
                        // console.log(row);
                        this.chartData.rows.push(row);
                    }
                } else if(this.selectCountry === 'russia') {
                    for(let name of this.russiaIndexNameList)
                        this.chartData.columns.push(name);
                    this.chartData.columns.push(this.russiaFundNameList[parseInt(this.selectFund)]);
                    this.chartData.columns.push('新聞事件');
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
                        this.chartData.rows.push(row);
                    }
                } else if(this.selectCountry === 'india') {
                    for(let name of this.indiaIndexNameList)
                        this.chartData.columns.push(name);
                    this.chartData.columns.push(this.indiaFundNameList[parseInt(this.selectFund)]);
                    this.chartData.columns.push('新聞事件');
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
                        // console.log(row);
                        this.chartData.rows.push(row);
                    }
                } else if(this.selectCountry === 'brazil') {
                    for(let name of this.brazilIndexNameList)
                        this.chartData.columns.push(name);
                    this.chartData.columns.push(this.brazilFundNameList[parseInt(this.selectFund)]);
                    this.chartData.columns.push('新聞事件');
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
                        // console.log(row);
                        this.chartData.rows.push(row);
                    }
                }
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>