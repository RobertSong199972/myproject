// pages/image/image.js
Component({

  /**
   * 页面的初始数据
   */
  data:{

  },
  lifetimes: {
    attached: function () {
      // console.log("yes")
    },
    detached: function () {
      // 在组件实例被从页面节点树移除时执行
    },
  },
  methods:{
    pic:function(options){
      wx.chooseImage({
        count:1,//默认为9
        sizeType:['original','compressed'],
        sourceType:['album','camera'],
        success: function(res) {
        //返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片       
          var tempFilePaths = res.tempFilePaths  //待识别图片路径
          console.log(tempFilePaths)
        },
        fail: function (res) {
          console.log(res.errMsg)
        }
      })
    }
  }
})