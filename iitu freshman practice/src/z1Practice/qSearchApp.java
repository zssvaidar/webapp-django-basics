package z1Practice;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

/**
 * practise task "Quick search app"
 * @author Zharassov Aidar
 * csse - 1703k
 */
public class qSearchApp extends Application 
{
	 static AnchorPane root ;
    @Override
    public void start(Stage stage) throws Exception 
    {
    	FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("Client1.fxml")); 
        fxmlLoader.setController(new sClientController());
        root = fxmlLoader.load();
        Scene scene = new Scene(root);
        stage.setScene(scene);
        stage.resizableProperty().set(false);
        stage.show();        
    }

    public static void main(String[] args) 
    {
        launch(args);
    }  
}