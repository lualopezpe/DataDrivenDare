output "postgresql_flex_server_fqdn" {
  value       = azurerm_postgresql_flexible_server.pg_flex.fqdn
  description = "The FQDN of Azure Database for PostgreSQL Flexible Server"
}

output "postgresql_flex_admin_username" {
  value       = azurerm_postgresql_flexible_server.pg_flex.administrator_login
  description = "The admin username for PostgreSQL Flexible Server"
  sensitive   = true
}

output "postgresql_flex_admin_password" {
  value       = azurerm_postgresql_flexible_server.pg_flex.administrator_password
  description = "The admin password for PostgreSQL Flexible Server"
  sensitive   = true
}
