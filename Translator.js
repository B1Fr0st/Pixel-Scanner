var scene = {
  
  art:[],
  
  palette:{
  },
  pixSize:0
  };


//this art was made with a custom designed pixel art creator, which exports art in this format. Credit to Loki (B1Fr0st) to making the translator and this program. https://github.com/B1Fr0st/Pixel-Scanner

function pixelArt(bitmap,palette,pixelSize){
    
    for(var i = 0; i < bitmap.length;i++){
        noStroke();
        for(var j = 0; j < bitmap[i].length;j++){
            fill(palette[bitmap[i][j]]);
            rect(j*pixelSize,i*pixelSize,pixelSize,pixelSize);
        }
    }
    var art = get(0,0,bitmap[0].length*pixelSize,bitmap.length*pixelSize);
    
    return art;
}
image(pixelArt(scene.art,scene.palette,scene.pixSize),0,0,width,height);
