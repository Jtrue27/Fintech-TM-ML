<template>
    <aside class="jAside">
        <el-menu default-active="5" class="el-menu-customize" theme="dark">
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-edit"></i>查看資料
                </template>
                <router-link :to="{name:'lineChart'}">
                    <el-menu-item index="1-1">
                        投資比例
                    </el-menu-item>
                </router-link>
                <router-link :to="{name:'pieChart'}">
                    <el-menu-item index="1-2">
                        購買人數
                    </el-menu-item>
                </router-link>
            </el-submenu>
            <router-link to='/'>
                <el-menu-item index="6">
                    <i class="el-icon-information"></i>
                    Home
                </el-menu-item>
            </router-link>
        </el-menu>
    </aside>
</template>
<script>
    export default {
        name: "leftSide",
        data() {
            return {
                msg: "hello",
            };
        },
        mounted() {
        },
        methods: {
            // handleOpen(key, keyPath) {
            //     // console.log(key, keyPath);
            // },
            // handleClose(key, keyPath) {
            //     // console.log(key, keyPath);
            // }
        }
    };
</script>
<style lang="scss" scoped>
    @import "~@/common/scss/variable";
    aside {
        position: relative;
        height: 100%;
        width: 100%;
        background-color: #324157;
    }

    a {
        color: inherit;
        text-decoration: none;
    }
</style>
