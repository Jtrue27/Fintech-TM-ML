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
        </div>
        定期定額扣款人數
        <ve-line :data="chartData" :extend="extend"></ve-line>
    </div>
</template>

<script>
    import { addMonths, getYear, getMonth } from 'date-fns';

    export default {
        name: "lineChart",
        data: function () {
            return {
                selectCountry: '中國',
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
                chinaFundNameList: [],
                chinaFundValueList: [],
                russiaFundNameList: [],
                russiaFundValueList: [],
                indiaFundNameList: [],
                indiaFundValueList: [],
                brazilFundNameList: [],
                brazilFundValueList: [],
                extend: {
                    legend: {
                        bottom: 0,
                        type: 'scroll'
                    }
                }
            }
        },
        mounted() {
            let json = require('../assets/json/china');
            for(let name in json) {
                this.chinaFundNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.chinaFundValueList.push(fundValueTempList);
            }
            json = require('../assets/json/russia');
            for(let name in json) {
                this.russiaFundNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.russiaFundValueList.push(fundValueTempList);
            }
            json = require('../assets/json/india');
            for(let name in json) {
                this.indiaFundNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.indiaFundValueList.push(fundValueTempList);
            }
            json = require('../assets/json/brazil');
            for(let name in json) {
                this.brazilFundNameList.push(name);
                let fundValueTempList = [];
                for(let value in json[name]) {
                    fundValueTempList.push(json[name][value]);
                }
                this.brazilFundValueList.push(fundValueTempList);
            }
            this.setChartData('china')
        },
        methods: {
            setChartData(country) {
                let columns = ['日期'];
                let rows = [];
                if(country === 'china') {
                    for(let name of this.chinaFundNameList) {
                        columns.push(name);
                    }
                    let date = new Date(2016, 3);
                    for(let i = 0; i <= 35; i++) {
                        date = addMonths(date, 1);
                        let fundObject = {
                            '日期': getYear(date).toString()+'/'+getMonth(date).toString()
                        };
                        for(let index in this.chinaFundNameList) {
                            fundObject[this.chinaFundNameList[index]] = this.chinaFundValueList[index][i]
                        }
                        rows.push(fundObject);
                    }
                } else if (country === 'russia') {
                    for(let name of this.russiaFundNameList) {
                        columns.push(name);
                    }
                    for(let i = 0; i <= 35; i++) {
                        let fundObject = {
                            '日期': i
                        };
                        for(let index in this.russiaFundNameList) {
                            fundObject[this.russiaFundNameList[index]] = this.russiaFundValueList[index][i]
                        }
                        rows.push(fundObject);
                    }
                } else if (country === 'india') {
                    for(let name of this.indiaFundNameList) {
                        columns.push(name);
                    }
                    for(let i = 0; i <= 35; i++) {
                        let fundObject = {
                            '日期': i
                        };
                        for(let index in this.indiaFundNameList) {
                            fundObject[this.indiaFundNameList[index]] = this.indiaFundValueList[index][i]
                        }
                        rows.push(fundObject);
                    }
                } else if (country === 'brazil') {
                    for(let name of this.brazilFundNameList) {
                        columns.push(name);
                    }
                    for(let i = 0; i <= 35; i++) {
                        let fundObject = {
                            '日期': i
                        };
                        for(let index in this.brazilFundNameList) {
                            fundObject[this.brazilFundNameList[index]] = this.brazilFundValueList[index][i]
                        }
                        rows.push(fundObject);
                    }
                }
                this.chartData.columns = columns;
                this.chartData.rows = rows;

            },
            changeCountry() {
                this.setChartData(this.selectCountry);
            }
        }
    }
</script>

<style scoped>

</style>