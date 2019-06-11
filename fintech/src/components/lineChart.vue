<template>
    <div>
        <div style="text-align: center">
            <el-select v-model="selectCountry" placeholder="請選擇國家">
                <el-option
                        v-for="item in optionCountry"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
        </div>
        定期定額扣款人數占比
        <ve-line :data="chartData"></ve-line>
    </div>
</template>

<script>
    export default {
        name: "lineChart",
        data: function () {
            return {
                selectCountry: '',
                chartData: {
                    columns: ['日期', '访问用户', '下单用户', '下单率'],
                    rows: [
                        { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
                        { '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 },
                        { '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 },
                        { '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 },
                        { '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 },
                        { '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 }
                    ]
                },
                optionCountry: [{
                    value: '中國',
                    label: '中國'
                }, {
                    value: '南非',
                    label: '南非'
                }, {
                    value: '俄羅斯',
                    label: '俄羅斯'
                }, {
                    value: '印度',
                    label: '印度'
                }, {
                    value: '巴西',
                    label: '巴西'
                }],
            }
        }
    }
</script>

<style scoped>

</style>