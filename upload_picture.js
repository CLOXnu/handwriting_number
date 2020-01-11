class Picture {
    constructor(img) {
        this.img = img;
        // document.getElementById('desc').innerHTML = "Upload success"
    }
    uploadPic(t) {
        let fileObj = t,
            windowURL = window.URL || window.webkitURL,
            dataURL,
            _img = document.getElementById(this.img);
        if (fileObj && fileObj.files && fileObj.files[0]) {
            dataURL = windowURL.createObjectURL(fileObj.files[0]);
            _img.setAttribute('src', dataURL);
            var jsonData = {
                "data" : dataURL
            }
            $.ajax({
                type: "GET",
                url: "/start.py",
                data: JSON.stringify(jsonData),
                contentType: 'application/json; charset=UTF-8',
                dataType: 'json',
                success: function(resData){
                    console.log('success')
                    let res = JSON.parse(resData)
                    document.getElementById('desc').innerHTML = "the result is " + res.result
                }
            })
        } else {
            dataURL = t.value;
            let imgObj = document.getElementById(this.img);
            imgObj.style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale)";
            imgObj.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = dataURL;
        }
    }
}
//调用方法：
document.getElementById('add-pic-btn').addEventListener("change", function () {
    let newPic = new Picture('add-pic-img');
    newPic.uploadPic(this);
});