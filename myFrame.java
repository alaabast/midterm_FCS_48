import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class myFrame extends JFrame {
      public static String m="dr";
    JButton eraser=new JButton("eraser");
    JButton draw=new JButton("draw");
    JButton color=new JButton("color");
    JButton plus=new JButton("plus");
    JButton minus=new JButton("minus");
    JPanel p = new JPanel();
   myPanel d = new myPanel();
    public myFrame(){
        setLayout(new GridLayout(2,1));
        p.setLayout(new FlowLayout(FlowLayout.CENTER,40,10));
        p.add(eraser);
        p.add(draw);
        p.add(color);
        p.add(plus);
        p.add(minus);
        eraser.addActionListener(new Ac());
        draw.addActionListener(new Ac());
        color.addActionListener(new Ac());
        plus.addActionListener(new Ac());
        minus.addActionListener(new Ac());
        p.setPreferredSize(new Dimension(100,100));

        add(d);
        add(p);
    }
public class Ac implements ActionListener{
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==eraser){
            setM("er");
        }
        if(e.getSource()==draw){
            setM("dr");

        }
        if(e.getSource()==color){
            setM("co");

        }
        if(e.getSource()==plus) {
            myPanel.setR(myPanel.getR() + 5);
        }
        if(e.setSource()==minus) {
            myPanel.setR(myPanel.getR()-5);
        }
                }

}
    public static String getM(){
        return m;
}

    public void setM(String m) {
        this.m = m;
    }
}
