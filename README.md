<h1>基于Flask 实现的随机图片API</h1>


<h2>使用方法</h2>
<p>寻找资源图片，根据服务器带宽选择。选太大的图片会导致加载太慢。</p>
<br>
<p>然后进行如下操作:</p>
<ol>
  <li>将PNG图片放入images文件夹内</li>
  <li>使用Python3运行Random_images.py</li>
  <li>访问IP地址:5002/API/images</li>
</ol>


<p>如果你没有安装Flask框架那么可以运行</p>
<code>
pip3 install flask
</code>
<br>
<p>修改端口可以修改</p>
<code>
Web.run(host='0.0.0.0', port=5001) #其中5001为监听端口号
</code>
<br>
<p>代码很简单的。基本一眼就能看懂。</p>
