terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "${var.prefix}RG"
  location = "East US"
}


resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

resource "azurerm_service_plan" "asp" {
  name                = "${var.prefix}-asp-${random_integer.ri.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "F1"
}

resource "azurerm_postgresql_flexible_server" "pg_flex" {
  name                   = "${var.prefix}-postgres-flex-${random_integer.ri.result}"
  resource_group_name    = azurerm_resource_group.rg.name
  location               = var.location
  version                = "12"
  storage_mb             = 32768
  administrator_login    = var.postgresql_login
  administrator_password = var.postgresql_pwd
  sku_name               = "B_Standard_B1ms"
  backup_retention_days  = 7

}

resource "azurerm_linux_web_app" "webapp" {
  name                = "${var.prefix}-webapp-${random_integer.ri.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.asp.id

  site_config {
    application_stack {
      docker_image     = var.docker_image_url
      docker_image_tag = "latest"
    }

    always_on = false

  }

  app_settings = {
    "SQLALCHEMY_DATABASE_URI"        = "postgresql://${var.postgresql_login}:${var.postgresql_pwd}@${azurerm_postgresql_flexible_server.pg_flex.fqdn}:5432/postgres"
    "SQLALCHEMY_TRACK_MODIFICATIONS" = "False"
    "DEBUG"                          = "False"
    "DOCKER_REGISTRY_SERVER_URL"     = "https://index.docker.io"


  }
}










