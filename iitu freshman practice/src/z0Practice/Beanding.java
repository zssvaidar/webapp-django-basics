package z0Practice;

import javafx.beans.binding.Bindings;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;

public class Beanding implements Runnable 
{
	
	static SimpleIntegerProperty[] numbers;
	@FXML static  GridPane gridPane;
	private int i;
	public Beanding(SimpleIntegerProperty[] numbers, GridPane gridPane)
	{
		this.numbers = numbers;	
		this.gridPane = gridPane;
	}
	
	public Beanding(int i) 
	{
		this.i = i;
		
	}

	@Override
	public void run() 
	{
		((Label)gridPane.getChildren().get(i)).textProperty().bind(Bindings.createObjectBinding(()->
		 { 						
			 
			 return  numbers[i].getValue().toString();	
			 
		 }, numbers[i] ));
	}
}

