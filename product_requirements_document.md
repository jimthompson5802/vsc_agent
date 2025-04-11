# Product Requirements Document

A flask application that allows a user to enter text into a text box and the application will echo back the text in a different text box with the string "echoed: " in front of it. The application should also have a button that, when clicked, will clear both text boxes.


## User Stories Table

| User Story ID | Description | Acceptance Criteria |
|---------------|-------------|----------------------|
| US-01         | As a user, I want to input text into a text box so that I can see it echoed back in another text box. | When text is entered in the first text box, the second text box displays "echoed: " followed by the entered text. |
| US-02         | As a user, I want to clear both text boxes so that I can reset the application. | When the "Clear" button is clicked, both text boxes are cleared. |
| US-03         | As a user, I want the application to handle empty input gracefully so that it does not break or behave unexpectedly. | When the first text box is empty and the button is clicked, the second text box displays "echoed: " without additional text. |
| US-04         | As a user, I want a simple and clean user interface so that I can use the application easily. | The application has two text boxes and a "Clear" button positioned below them. The text boxes are large enough to accommodate a reasonable amount of text. |

