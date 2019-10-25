## README

由于这个网页实现过于复杂(用了service worker带wasm wasm接口还很麻烦) 所以考虑直接在网页上操作进行计算 再返回给主程序

启动mid.py作为中间件进行交互

在[三次方计算器](<https://www.alpertron.com.ar/FCUBES.HTM>)的console里面直接复制web.js内容

将web.js里3替换成2 复制到[二次方计算器](<https://www.alpertron.com.ar/FSQUARES.HTM>)的console

直接运行do.py即可开始

得到第三个flag后会sleep

