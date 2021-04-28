function automateForm() {

    var app = SpreadsheetApp;
    var form = FormApp.create('MyFav');
  
    var item = form.addCheckboxItem();
    var activeSheet = app.getActiveSpreadsheet().getActiveSheet();
    var option1 = activeSheet.getRange(1,1).getValue()
    var option2 = activeSheet.getRange(3,1).getValue()
    var option3 = activeSheet.getRange(5,1).getValue()
    var option4 = activeSheet.getRange(7,1).getValue()
    var option5 = activeSheet.getRange(9,1).getValue()
  
  
  
    item.setTitle("Who is your favorite actor?");
    item.setChoices([
      item.createChoice(option1),
      item.createChoice(option2),
      item.createChoice(option3),
      item.createChoice(option4),
      item.createChoice(option5)
    ]);
  
    let formURL = form.getPublishedUrl();
    
    // !!! Add here the additional recipients using the plus sign and concatenate email addresses with commas
    // e.g. recipients = "emai1@gmail.com" + "," + "email2@yahoo.com" + "," + "email3@outlook.com" + "," + ...
    let recipients = "kaankoksal23@gmail.com"
  
    MailApp.sendEmail({
      to: recipients,
      subject: "form test",
      body: "Form URL is " + formURL
    });
  
  }
  