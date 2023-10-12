variable "prefix" {
  description = "Resources prefix"
  default     = "datadrivendare"
}

variable "location" {
  description = "Azure resources location"
  default     = "East US"
}

variable "docker_image_url" {
  description = "Docker image url"
  default     = "lualopezpe/datadrivendare"
}

variable "postgresql_login" {
  description = "Database username"
  default     = "lualopezpe"
}

variable "postgresql_pwd" {
  description = "Database password"
  default     = "Lu4lop3zp3*"
}