import java.applet.Applet;
import java.awt.Graphics;


public class HelloWorldApplet extends Applet {
    public void init() {}
    public void stop() {}
    public void paint(Graphics g){

	g.drawString("Hey hey hey",20,20);
	g.drawString("Hello World!",20,40);
    
    }
    
}
