import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class meditate extends PApplet {

int screen = 0;
/*
Screens:
0 - Start
1 - Meditate
2 - Done
*/
int minutes = 2;

Button minusTime;
Button plusTime;
Button start;

Button back = new Button(0,0,0,0,"",0,false);
Button restart = new Button(0,0,0,0,"",0,false);
PImage restartIcon;

int ellipseSize = 100;
float change = 0.5f;

int startTime = 0;
int timeWaiting = 0;

public void setup(){
  
  frameRate(25);
  restartIcon = loadImage("restart-icon.png");
}

public void draw(){
  if(screen == 0){
    drawStartScreen();
  }
  if(screen == 1){
    drawMeditateScreen();
  }
  if(screen == 2){
    drawDoneScreen();
  }
}

public void drawStartScreen(){
  background(33, 175, 222);
  fill(255);
  textAlign(CENTER);
  textSize(60);
  text("Phokus", width/2, height/2-100);
  textSize(40);
  text("Meditate", width/2, height/2-40);
  minusTime = new Button(width/2-100, height/2+50, 70, 70, "-", 60, true);
  plusTime = new Button(width/2+100, height/2+50, 70, 70, "+", 60, true);
  minusTime.display();
  plusTime.display();
  fill(255);
  textAlign(CENTER);
  textSize(60);
  text(minutes, width/2, height/2+50);
  textSize(20);
  text("min(s)", width/2, height/2+80);
  start = new Button(width/2, height/2+150, 300, 100, "Start", 60, true);
  start.display();
}

public void drawMeditateScreen(){
  background(33, 175, 222);
  ellipseMode(CENTER);
  fill(255);
  noStroke();
  ellipse(width/2, height/2, ellipseSize, ellipseSize);
  ellipseSize += change;
  if(ellipseSize == 190){
    change = -1;
    timeWaiting += 1;
    delay(1000);
  }
  if(ellipseSize == 100){
    change = 1;
    timeWaiting += 1;
    delay(1000);
  }
  fill(255);
  textSize(40);
  if(change == -1){
    text("Now slowly exhale...", width/2, height/2+200);
  }
  if(change == 1){
    text("Now take a deep breath in...", width/2, height/2+200);
  }
  int secondsElapsed = (millis()-startTime+timeWaiting)/1000;
  int secondsRemaining = minutes*60 - secondsElapsed;
  if(secondsElapsed/60 == minutes){
    screen = 2;
  }
  textAlign(RIGHT);
  int minutes = floor(secondsRemaining/60);
  int seconds = secondsRemaining%60;
  String timeElapsed = str(minutes) + ":";
  if(seconds < 10){
    timeElapsed += "0";
  }
  timeElapsed += str(seconds);
  text(timeElapsed, width-10, 35);
  back = new Button(60, 30, 100, 40, "<- Back", 30, true);
  back.display();
}

public void drawDoneScreen(){
  background(33, 175, 222);
  fill(255);
  textSize(80);
  textAlign(CENTER);
  text("Done!", width/2, height/2);
  restart = new Button(width/2, height/2+175, 275, 80, "      Restart", 60, true);
  restart.display();
  imageMode(CENTER);
  restartIcon.resize(50,50);
  image(restartIcon, width/2-90, height/2+182);
}

public void mousePressed(){
  if(screen == 0){
    if(minusTime.mouseOver()){
        if(minutes > 1){
          minutes--;
        }
      }
    if(plusTime.mouseOver()){
      if(minutes < 5){
        minutes++;
      }
    }
    if(start.mouseOver()){
      screen = 1;
      startTime = millis();
    }
  }
  if(screen == 1){
    if(back.mouseOver()){
      reset();
      screen = 0;
    }
  }
  if(screen == 2){
    if(restart.mouseOver()){
      reset();
      screen = 0;
    }
  }
}

public void reset(){
  minutes = 2;
  ellipseSize = 100;
  change = 0.5f;
  startTime = 0;
  timeWaiting = 0;
}

class Button {
    int buttonX;
    int buttonY;
    int buttonWidth;
    int buttonHeight;
    String text;
    int textSize;
    boolean hoverShading;
    
    Button(int x, int y, int w, int h, String t, int ts, boolean hs){
        buttonX = x;
        buttonY = y;
        buttonWidth = w;
        buttonHeight = h;
        text = t;
        textSize = ts;
        hoverShading = hs;
    }
    
    public void display(){
        stroke(255);
        strokeWeight(2);
        if(hoverShading){
            if (this.mouseOver()) {
                fill(29, 155, 196);
            }
            else{
                fill(33, 175, 222);
            }
        }
        else{
            fill(255);
        }
        rectMode(CENTER);
        rect(buttonX, buttonY, buttonWidth, buttonHeight);
        fill(255);
        textSize(textSize);
        textAlign(CENTER, CENTER);
        text(text, buttonX, buttonY);
    }
    
    public boolean mouseOver()  {
        return mouseX >= buttonX-buttonWidth/2 && mouseX <= buttonX+buttonWidth/2 && mouseY >= buttonY-buttonHeight/2 && mouseY <= buttonY+buttonHeight/2;
    }
}
  public void settings() {  size(800,600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "meditate" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
