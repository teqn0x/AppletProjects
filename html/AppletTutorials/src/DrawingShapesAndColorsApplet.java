import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Font;


public class DrawingShapesAndColorsApplet extends Applet {


    //Colors that are needed anywhere in this class
    Font bigFont;
    Color redColor;
    Color weirdColor;
    Color bkgColor;

    public void init(){
	//initialize the variables here
	bigFont=new Font("Comic Sans MS",Font.BOLD,16);
	redColor = Color.red;
	weirdColor = new Color(60,70,80);
	bkgColor = Color.blue;
	setBackground(bkgColor);
    }
    
    public void stop() {}

    public void paint(Graphics g){
	g.setFont(bigFont);
	g.drawString("Shapes and Colors",80,20);
	
	g.setColor(redColor);
	
	g.drawRect(100,100,100,100); //Draw a rectangle x,y 100,100, w,l 100,100
	
	g.fillRect(110,110,80,80);   //Draw and fill a rectangle, x,y 110,110, w,l 80,80
	
	g.setColor(weirdColor);
	
	g.fillArc(120,120,60,60,0,270);
	
	g.setColor(Color.yellow); //Color does not have to be a predefined variable, can directly input from Color
	
	g.drawLine(140,140,160,160);


	// Resetting the color at the end can be vital for the next time the applet paints something.
	// The applet is actually repainted after a part isn't visible anymore,
	// which happens often after scrolling or minimizing the browser.
	g.setColor(Color.black);
    }

}

	
	
