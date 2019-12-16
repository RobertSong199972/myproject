//app.js
App({
  onLaunch: function () {
    var that=this
    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上的基础库以使用云能力')
    } else {
      wx.cloud.init({
        // env 参数说明：
        //   env 参数决定接下来小程序发起的云开发调用（wx.cloud.xxx）会默认请求到哪个云环境的资源
        //   此处请填入环境 ID, 环境 ID 可打开云控制台查看
        //   如不填则使用默认环境（第一个创建的环境）
        env: 'gabage-2020',
        traceUser: true,
      })
    }

    this.globalData = {}
    that.globalData.cookie1 = wx.getStorageSync("coockie1")
    that.globalData.cookie2 = wx.getStorageSync("coockie2")
  },
  watch: function (method) {
    var obj = this.globalData;
    Object.defineProperty(obj, "show", {
      configurable: true,
      enumerable: true,
      set: function (value) {
        this._show = value;
        
        method(value);
      },
      get: function () {
        // 可以在这里打印一些东西，然后在其他界面调用getApp().globalData.name的时候，这里就会执行。
        return this._show
      }
    })
  },
  globalData: {
    isLogin:false,
    avatarUrl:'',
    nickName:'',
    _show:false,
  }
})
