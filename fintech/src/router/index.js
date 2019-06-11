import Vue from 'vue'
import Router from 'vue-router'

import home from '@/components/home';
import lineChart from '@/components/lineChart';
import pieChart from '@/components/pieChart';

Vue.use(Router);

export default new Router({
    // 严格模式会深度监测状态树来检测不合规的状态变更
    strict: process.env.NODE_ENV !== 'production',
    routes: [{
        path: '/',
        component: home,
        children: [{
            path: '/lineChart',
            name: 'lineChart',
            component: lineChart,
        },{
            path: '/pieChart',
            name: 'pieChart',
            component: pieChart,
        }]
    }]
})
