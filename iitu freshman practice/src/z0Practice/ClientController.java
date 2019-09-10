package z0Practice;

import java.util.Random;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Text;

/**
 *
 * @author PChelper.kz
 */
public class ClientController 
{
	@FXML 
	Text text;
	@FXML
	Button ok, ok1, ok2, ok3;
	@FXML 
	GridPane gridPane;
	@FXML 
	Label label_1,label_2,label_3,label_4,label_5,
		  label_6,label_7,label_8,label_9,label_10,
		  label_11,label_12,label_13,label_14,label_15,
		  label_16,label_17,label_18,label_19,label_20,
		  label_21,label_22,label_23,label_24,label_25,
		  label_26,label_27,label_28,label_29,label_30,
		  stateLabel;
	private ObservableList <Label>labels = FXCollections.observableArrayList();

	
	static int i=0;
	@FXML public void initialize() 
	{
		ok.setStyle(" -fx-background-color: \r\n" + 
				"        #3c7fb1,\r\n" + 
				"        linear-gradient(#fafdfe, #e8f5fc),\r\n" + 
				"        linear-gradient(#eaf6fd 0%, #d9f0fc 49%, #bee6fd 50%, #a7d9f5 100%);\r\n"+ 
				"    -fx-text-fill: black;\r\n");

		SimpleIntegerProperty []numbers = new SimpleIntegerProperty[25];
		Beanding cellBinding = new Beanding(numbers, gridPane);
		i=0;
		for(i = 0; i<25 ; i++ ) 
		{
			numbers[i] = new SimpleIntegerProperty((new Random(i)).nextInt(100)+1);
			new Thread(new Beanding(i)).start();
			
		}
		
	
		ok.setOnAction(e->{
			stateLabel.setText("Insertionaly sorted ascendant order");
			int buff1,buff2;
			 for (int i = 1; i < 25; i++) 
				 for(int ii = i ; ii > 0 ; ii--)
				 {
					 buff1 = numbers[ii].getValue();
					 buff2 = numbers[ii-1].getValue();
					 if(buff1 < buff2) 
					 {	
						numbers[ii].setValue(buff2);
						numbers[ii-1].setValue(buff1); 
					}
				 }	
		     });
		ok1.setOnAction(e->{
			stateLabel.setText("Insertionaly sorted descendant order");
			int buff1,buff2;
			 for (int i = 1; i < 25; i++) 
				 for(int ii = i ; ii > 0 ; ii--)
				 {
					 buff1 = numbers[ii].getValue();
					 buff2 = numbers[ii-1].getValue();
					 if(buff1 > buff2) 
					 {	
						 numbers[ii].setValue(buff2);
						 numbers[ii-1].setValue(buff1); 
					 }
				 }	
			 });
		ok2.setOnAction(e->{
			stateLabel.setText("Selectionaly sorted ascendant order");
		
				for (int i = 0; i < 24; i++)
		        {
					int index = i;
		            for (int ii = i + 1; ii < 25; ii++) {
		                if (numbers[ii].getValue() < numbers[index].getValue()) 
		                    index = ii;
		      
		            int smallerNumber = numbers[index].getValue();  
		            numbers[index].set(numbers[i].getValue());
		            numbers[i].setValue(smallerNumber);}
		        }
			});		
		ok3.setOnAction(e->{
			stateLabel.setText("Selectionaly sorted descendant order");
			
			for (int i = 0; i < 24; i++)
	        {
				int index = i;
	            for (int ii = i + 1; ii < 25; ii++) {
	                if (numbers[ii].getValue() > numbers[index].getValue()) 
	                    index = ii;
	      
	            int smallerNumber = numbers[index].getValue();  
	            numbers[index].set(numbers[i].getValue());
	            numbers[i].setValue(smallerNumber);}
	        }
		});
	}
}
