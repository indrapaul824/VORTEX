let model;
async function loadModel() {
    console.log('Loading model...');
    model = undefined;
    model = await tf.loadLayersModel('./vortex/artifacts/border_box/tfjs/detector/model.json');
    console.log('Model loaded.');
}

async function loadFile() {
    console.log("image is in loadfile..");
    document.getElementById("select-file-box").style.display = "table-cell";
    document.getElementById("predict-box").style.display = "table-cell";
    document.getElementById("prediction").innerHTML =
      "Click predict to find the type of Skin Cancer!";
    var fileInputElement = document.getElementById("select-file-image");
    console.log(fileInputElement.files[0]);
    renderImage(fileInputElement.files[0]);
  }