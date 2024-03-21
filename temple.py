# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : temple.py
# @Author: yan xiaohao
# @Date  : 2024/3/21
home = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer" />
    <title>B站</title>
    <link rel="stylesheet" href="./css/index.css">
    <link rel="stylesheet" href="./fonts/iconfont.css">
</head>
<body>
    <!-- 1. 头部固定 -->
    <header>
        <div class="top">
            <div class="left">
                <a href="#"><i class="iconfont Navbar_logo"></i></a>
            </div>

            <div class="right">
                <a href="#"><i class="iconfont ic_search_tab"></i></a>
<!--                <a href="#" class="login"><img src="./images/login.png" alt=""></a>-->
<!--                <a href="#" class="download"><img src="./images/download.png" alt=""></a>-->
            </div>
        </div>

        <div class="botton">
            <div class="tab">
                <ul>
                    <li><a href="#" class="current">首页</a></li>
                    <li><a href="#">动画</a></li>
                    <li><a href="#">番剧</a></li>
                    <li><a href="#">国创</a></li>
                    <li><a href="#">音乐</a></li>
                </ul>
            </div>
            <div class="more">
                <a href="#"><i class="iconfont general_pulldown_s"></i></a>
            </div>
        </div>
    </header>

    <!-- tab: 菜单的个数要和内容的个数相等 -->
    <!-- 2. 视频 -->
    <div class="video_content">
        <!-- 一份视频, 共计5个菜单, 应该有5份视频的video_list -->
        <div class="video_list">
            {}
        </div>

    </div>
</body>
</html>
'''
# img,price,original_price,name
item = '''
            <a href="#">
                <div class="pic">
                    <img src="{}" loading="lazy" alt="">
                    <div class="count">
                        <p>
                            <i class="iconfont icon_shipin_bofangshu"></i>
                            <span>现价:{}</span>
                        </p>
                        <p>
                            <i class="iconfont icon_shipin_danmushu"></i>
                            <span>原价:{}</span>
                        </p>
                    </div>
                </div>
                <div class="txt ellipsis-2">
                    <p>{}</p>
                </div>
            </a>
'''