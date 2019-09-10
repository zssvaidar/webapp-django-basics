package z1Practice;

import java.util.Arrays;
import java.util.Random;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Text;

/**
 *
 * @author PChelper.kz
 */
public class sClientController 
{
	@FXML 
	Text text;

	@FXML 
	GridPane gridPane;
	@FXML Label w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,
	label1,label2,label3,label4,label5,label6,label7,label8,label9,
	label10,label11,label12,label13,label14,label15,label16,label17;
	@FXML TextField field;int []sortedArray =new int[17];
	@FXML Button generateSequence, findNumber, findNumber1;
	private ObservableList <Label>labels = FXCollections.observableArrayList();
	private ObservableList <Label>indicatorLabel = FXCollections.observableArrayList();
	private ObservableList <Integer>numbers = FXCollections.observableArrayList();
	int number;
	private  void initializeRsequence() 
	{
		numbers.clear();	
		for(int i = 0; i<17 ; i++ )
		{		
			numbers.add(new Random().nextInt(998)+1);
			labels.get(i).setText(Integer.toString(numbers.get(i)));			
		}

	}

	
	private int ternary_search(int l,int r, int x)
	{		
	    if(r>=l)
	    {
	        int mid1 = l + (r-l)/3;
	        int mid2 = r -  (r-l)/3;
	        if(sortedArray[mid1] == x)
	            return mid1;
	        if(sortedArray[mid2] == x)
	            return mid2;
	        if(x<sortedArray[mid1])
	            return ternary_search(l,mid1-1,x);
	        else if(x>sortedArray[mid2])
	            return ternary_search(mid2+1,r,x);
	        else
	            return ternary_search(mid1+1,mid2-1,x);
	    }
	    return -1;
	}
	private void sortFillArray() 
	{
		for (int i = 0; i < 17; i++) 
			sortedArray[i] = numbers.get(i);
		int smallerNumber = 0 ;
		for (int i = 0; i < 16; i++)      
			for (int ii = 0; ii < 16; ii++) 
				if (sortedArray[ii] > sortedArray[ii+1]) 
                {    
                smallerNumber = sortedArray[ii]; 
                sortedArray[ii] = sortedArray[ii+1];
                sortedArray[ii+1] = smallerNumber;
                }
	}
	private void SearchMark(boolean binary) 
	{	
		try
		{
			sortFillArray();
			int foundIndex;
			if(binary) foundIndex = Arrays.binarySearch(sortedArray, number);
			else  foundIndex = ternary_search(0,16,number);
			for(int i = 0; i < 17; i++ ) 
			{
				if(numbers.get(i).equals(sortedArray[foundIndex]))
				{
					foundIndex = i;
					break;
				}
			}	
		
		
			switch(foundIndex) 
			{
			case 0: w1.setStyle("-fx-background-color:red;");break;
			case 1: w2.setStyle("-fx-background-color:red;");break;
			case 2: w3.setStyle("-fx-background-color:red;");break;
			case 3: w4.setStyle("-fx-background-color:red;");break;
			case 4: w5.setStyle("-fx-background-color:red;");break;
			case 5: w6.setStyle("-fx-background-color:red;");break;
			case 6: w7.setStyle("-fx-background-color:red;");break;
			case 7: w8.setStyle("-fx-background-color:red;");break;
			case 8: w9.setStyle("-fx-background-color:red;");break;
			case 9: w10.setStyle("-fx-background-color:red;");break;
			case 10: w11.setStyle("-fx-background-color:red;");break;
			case 11: w12.setStyle("-fx-background-color:red;");break;
			case 12: w13.setStyle("-fx-background-color:red;");break;
			case 13: w14.setStyle("-fx-background-color:red;");break;
			case 14: w15.setStyle("-fx-background-color:red;");break;
			case 15: w16.setStyle("-fx-background-color:red;");break;
			case 16: w17.setStyle("-fx-background-color:red;");break;
			}
		}catch(java.lang.IndexOutOfBoundsException e) {}
	}
	private void wipeindicatorColor() 
	{
		 w1.setStyle("-fx-background-color:white;");
		 w2.setStyle("-fx-background-color:white;");
		 w3.setStyle("-fx-background-color:white;");
		 w4.setStyle("-fx-background-color:white;");
		 w5.setStyle("-fx-background-color:white;");
		 w6.setStyle("-fx-background-color:white;");
		 w7.setStyle("-fx-background-color:white;");
		 w8.setStyle("-fx-background-color:white;");
		 w9.setStyle("-fx-background-color:white;");
		 w10.setStyle("-fx-background-color:white;");
		 w11.setStyle("-fx-background-color:white;");
		 w12.setStyle("-fx-background-color:white;");
		 w13.setStyle("-fx-background-color:white;");
		 w14.setStyle("-fx-background-color:white;");
		 w15.setStyle("-fx-background-color:white;");
		 w16.setStyle("-fx-background-color:white;");
		 w17.setStyle("-fx-background-color:white;");
			
	}
	

	@FXML 
	public void initialize() 
	{	
		labels.addAll(label1,label2,label3,label4,label5,label6,label7,label8,label9,
					label10,label11,label12,label13,label14,label15,label16,label17);
		indicatorLabel.addAll(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17);
		
		initializeRsequence();
			
		generateSequence.setOnAction(e->{		
			initializeRsequence();
		});
		
		findNumber.setOnAction(e->{
			wipeindicatorColor();	
			SearchMark(true);
			
		});
		
		findNumber1.setOnAction(e->{
			wipeindicatorColor();			
			SearchMark(false);
			
		});
		
		field.textProperty().addListener((observable, oldValue, newValue) -> {
			   try{
				   number = Integer.parseInt(newValue);
			   }catch(Exception e) {}
				
			});
		
	} 
}
