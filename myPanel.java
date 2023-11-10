import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;


public class myPanel extends JPanel {
    public int x, y;
    public static int r=10;

    public static void setR(int m) {
        r = m;
    }

    public static int getR() {
        return r;
    }

    public myPanel() {

        setPreferredSize(new Dimension(500,250));
        setBackground(Color.WHITE);
        addMouseMotionListener(new MouseMotionAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                x = e.getX();
                y = e.getY();
                repaint();

                }

        });
    }

    @Override
    protected void paintComponent(Graphics g) {
        String mode = myFrame.getM();

        if (mode.equals("er")) {
            g.setColor(Color.WHITE);
        }
        if (mode.equals("co")) {
            g.setColor(new Color((int) (Math.random() * 256), (int) (Math.random() * 256), (int) (Math.random() * 256)));
        }
        if(mode.equals("dr"))
        {g.setColor(Color.BLACK);}
        g.fillOval(x, y, r, r);
    }
}