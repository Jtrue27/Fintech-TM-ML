<template>
    <div>
        <div style="text-align: center">
            <el-select v-model="selectYear" placeholder="請選擇年份" @change="changeYear">
                <el-option
                        v-for="item in optionYear"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
            <el-select v-model="selectMonth" v-bind:disabled="isDisable" placeholder="請選擇月份" @change="changeMonth">
                <el-option
                        v-for="item in optionMonth"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                        :disabled="item.disabled">
                </el-option>
            </el-select>
        </div>
        定期定額扣款人數占比
        <ve-pie :data="chartData"></ve-pie>
    </div>
</template>
<script>
    export default {
        data () {
            return {
                selectYear: '',
                selectMonth: '',
                isDisable: true,
                chartData: {
                    columns: ['name', 'value'],
                    rows: [
                        { 'name': '中國', 'value': 0 },
                        { 'name': '印度', 'value': 0 },
                        { 'name': '巴西', 'value': 0 },
                        { 'name': '俄羅斯', 'value': 0 }
                    ]
                },
                countryName: [
                    '中國', '印度', '巴西', '俄羅斯'
                ],
                chinaData: [],
                brazilData: [],
                indiaData: [],
                russiaData: [],
                optionYear: [{
                    value: '2016',
                    label: '2016'
                }, {
                    value: '2017',
                    label: '2017'
                }, {
                    value: '2018',
                    label: '2018'
                }, {
                    value: '2019',
                    label: '2019'
                }],
                optionMonth: [{
                    value: '1',
                    label: '1',
                    disabled: false
                }, {
                    value: '2',
                    label: '2',
                    disabled: false
                }, {
                    value: '3',
                    label: '3',
                    disabled: false
                }, {
                    value: '4',
                    label: '4',
                    disabled: false
                }, {
                    value: '5',
                    label: '5',
                    disabled: false
                }, {
                    value: '6',
                    label: '6',
                    disabled: false
                }, {
                    value: '7',
                    label: '7',
                    disabled: false
                }, {
                    value: '8',
                    label: '8',
                    disabled: false
                }, {
                    value: '9',
                    label: '9',
                    disabled: false
                }, {
                    value: '10',
                    label: '10',
                    disabled: false
                }, {
                    value: '11',
                    label: '11',
                    disabled: false
                }, {
                    value: '12',
                    label: '12',
                    disabled: false
                }]
            }
        },
        mounted() {
            let json = require('../assets/json/people');
            for(let i = 0; i <= 35; i++) {
                this.chinaData.push(json.China[i.toString()]);
                this.brazilData.push(json.Brazil[i.toString()]);
                this.indiaData.push(json.India[i.toString()]);
                this.russiaData.push(json.Russia[i.toString()]);
            }
        },
        methods: {
            changeYear() {
                this.isDisable = this.selectYear === '';
                if (this.selectYear === '2016') {
                    for (let i = 0; i < this.optionMonth.length; i++) {
                        this.optionMonth[i].disabled = i < 3;
                    }
                    if (parseInt(this.selectMonth) <= 3) {
                        this.selectMonth = '';
                    }
                } else if (this.selectYear === '2019') {
                    for (let i = 0; i < this.optionMonth.length; i++) {
                        this.optionMonth[i].disabled = i >= 3;
                    }
                    if (parseInt(this.selectMonth) > 3) {
                        this.selectMonth = '';
                    }
                } else {
                    for (let i = 0; i < this.optionMonth.length; i++) {
                        this.optionMonth[i].disabled = false;
                    }
                }
            },
            changeMonth() {
                let index = 0;
                if(this.selectYear === '2016') {
                    index = parseInt(this.selectMonth) - 4;
                } else {
                    index = (parseInt(this.selectYear) - 2017) * 12 + 8 + parseInt(this.selectMonth);
                }
                this.chartData = {
                    columns: ['name', 'value'],
                    rows: []
                };
                let data = {
                    name: this.countryName[0],
                    value: this.chinaData[index]
                };
                this.chartData.rows.push(data);
                data = {
                    name: this.countryName[1],
                    value: this.indiaData[index]
                };
                this.chartData.rows.push(data);
                data = {
                    name: this.countryName[2],
                    value: this.brazilData[index]
                };
                this.chartData.rows.push(data);
                data = {
                    name: this.countryName[3],
                    value: this.russiaData[index]
                };
                this.chartData.rows.push(data);
            }
        }
    }
</script>
<style lang="scss" scoped>

</style>
