import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class BallBounce extends JComponent {

   private static final long serialVersionUID = 1L;
   private static final int PREF_W = 900;
   private static final int PREF_H = 700;
   private static final int TIMER_DELAY = 30;
   public int rectX = 10;
   public int rectY = 10;
   public int changeX = 2;
   public int changeY = 2;
   public int width = 8;
   public int height = 10;

   public BallBounce() {
      new Timer(TIMER_DELAY, new ActionListener() {

         @Override
         public void actionPerformed(ActionEvent actEvt) {
            rectX += changeX;
            rectY += changeY;

            if (rectX < 0 || rectX > PREF_W - width) {
               changeX *= -1;
            } else if (rectY < 0 || rectY > PREF_H - height) {
               changeY *= -1;
            }
            repaint();
         }
      }).start();
   }


   @Override
   public Dimension getPreferredSize() {
      return new Dimension(PREF_W, PREF_H);
   }

   public void paintComponent(Graphics g) {
      super.paintComponent(g);
      g.setColor(Color.red);
      g.drawRect(rectX, rectY, width, height);
      g.fillRect(rectX, rectY, width, height);
   }

   public int getRectX() {
      return rectX;
   }

   public void setRectX(int rectX) {
      this.rectX = rectX;
   }

   public int getRectY() {
      return rectY;
   }

   public void setRectY(int rectY) {
      this.rectY = rectY;
   }

   private static void createAndShowGui() {
      Gunman mainPanel = new Gunman();

      JFrame frame = new JFrame("BallBounce");
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.getContentPane().add(mainPanel);
      frame.pack();
      frame.setLocationByPlatform(true);
      frame.setVisible(true);
   }

   public static void main(String[] args) {
      SwingUtilities.invokeLater(new Runnable() {
         public void run() {
            createAndShowGui();
         }
      });
   }

}
