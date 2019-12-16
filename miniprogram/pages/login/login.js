// pages/login/login.js
const db = wx.cloud.database()
const userCollection = db.collection('user')
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    avatarUrl: '',
    userInfo: ""
  },
  goToindex: function(e) {
    this.setData({
      modalName: null
    }, () => {
      wx.redirectTo({
        url: '../index/index',
      })
    })
  },
  hideModal(e) {
    console.log(e)
    this.setData({
      modalName: null
    })
  },
  onGetUserInfo: function(e) {
    if (e.detail.userInfo) {
      this.setData({
        logged: true,
        avatarUrl: e.detail.userInfo.avatarUrl,
        userInfo: e.detail.userInfo
      })
      console.log(this.data.avatarUrl)
      wx.setStorage({
        key: 'coockie1',
        data: e.detail.userInfo
      })

      // 调用云函数
      wx.cloud.callFunction({
        name: 'login',
        data: {},
        success: res => {
          wx.setStorage({
            key: 'coockie2',
            data: res.result.openid,
            success: function(res) {
              app.globalData.cookie1 = wx.getStorageSync("coockie1")
              app.globalData.cookie2 = wx.getStorageSync("coockie2")

              userCollection.where({
                _openid: app.globalData.cookie2
              }).get().then(res => {
                console.log(res)
                if (res.data.length == 0) {
                  userCollection.add({
                    data: {
                      avatarUrl: app.globalData.cookie1.avatarUrl,
                      penName: app.globalData.cookie1.nickName
                    },
                    success: function(res) {
                      console.log(res)
                    }
                  })
                }
                wx.redirectTo({
                  url: '../index/index',
                })
              })

            }
          })
        },
        fail: err => {
          console.log(fail)
        }
      })
    } else {
      this.setData({
        modalName: 'DialogModal'
      })
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function() {
    // wx.getStorage({
    //   key: 'coockie1',
    //   success: function(res) {
    //     console.log(res.data)
    //   }
    // }) 
    // wx.getStorage({
    //   key: 'coockie2',
    //   success: function (res) {
    //     console.log(res.data)
    //   }
    // }) 
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function() {

  }
})