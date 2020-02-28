library(shiny)
library(shinyjs)
library(httr)
library(jsonlite)
library(lubridate)

CreateUser  <- function(data) {
  
  GET(url = url, path = path)
}


ui <- fluidPage(
  headerPanel('Registration'),
  sidebarPanel(
  textInput("name", "Name", ""),
  textInput("email", "Email", ""),
  textInput("password", "Password", ""),
  textInput("confirm_password", "Conform Password", ""),
  actionButton("submit", "Submit"),
  )
 
)


server <- function(input, output, session) {
  observeEvent(input$submit,{
    if (input$password == input$confirm_password){
        var = CreateUser(input)
    }
  }
  
  
  )

  
}

shinyApp(ui = ui, server = server)
  