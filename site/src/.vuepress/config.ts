import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
    base: "/",

    lang: "zh-CN",
    title: "Nuitka中文文档",
    description: "Nuitka命令行帮助文档中文翻译",

    head: [
        ["link", { rel: "icon", href: "/logo.svg" }],
        ["link", { rel: "icon", type: "image/svg+xml", href: "/logo.svg" }],
    ],

    theme,

    // 如果你需要在本地开发时使用其他端口，请取消下方注释
    // port: 8080,

    // 如果你需要在本地开发时使用其他主机名，请取消下方注释
    // host: "0.0.0.0",

    // 和 PWA 一起启用
    shouldPrefetch: false,
});
