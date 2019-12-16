// pages/welcome/welcome.js
const db = wx.cloud.database()
const userCollection = db.collection('user')
var app = getApp();



Component({

  /**
   * 页面的初始数据
   */
  data: {
    avatarUrl:'',
    modalName:null,
    isLogin: false,
    nickName: '',
  },
  
  lifetimes: {
    attached: function () {
      if (app.globalData.cookie1 && app.globalData.cookie2) {
        this.setData({
          isLogin: true,
          avatarUrl: app.globalData.cookie1.avatarUrl,
          nickName: app.globalData.cookie1.nickName
        })
      } else {
        this.setData({
          modalName: "DialogModal"
        })
      }
    },
    detached: function () {
      // 在组件实例被从页面节点树移除时执行
    },
  },
  methods:{
    showModal(e) {
      console.log(e)
      if (this.data.isLogin) {
        this.setData({
          modalName: e.currentTarget.dataset.target
        })
        app.globalData.show=true
      } else {
        this.setData({
          modalName: "DialogModal"
        })
      }
      // console.log(this.data.modalName)
    },
    hideModal(e) {
      console.log(e)
      this.setData({
        modalName: null
      })
      app.globalData.show = false
    },
    goToLogin: function (e) {
      this.setData({
        modalName: null
      }, () => {
        wx.redirectTo({
          url: '/pages/login/login',
        })
      })
    },
    logOut(e) {
      wx.clearStorageSync()
      wx.redirectTo({
        url: '/pages/login/login',
      })
    },
    tomap: function () {
      wx.navigateTo({  //navigateTo可保留返回键
        url: '../map/map',
      })
    },
    totest:function(){
      wx.navigateTo({
        url: '../test/test',
      })
    },
    todata: function () {
      wx.navigateTo({
        url: '../data/data',
      })
    },
    tous: function () {
      wx.navigateTo({
        url: '../us/us',
      })
    }
  },
  
  /**
   * 生命周期函数--监听页面加载
   */
  

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {


  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {


  },

  /**
   * 生命周期函数--监听页面隐藏
   */

})