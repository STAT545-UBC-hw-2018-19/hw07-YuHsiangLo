#' Country geographic information
#' 
#' Data frame of Gapminder country names, average latitudes and longitudes, and surface areas:
#' \describe{
#' \item{latitude}{Average latitude.}
#' \item{longitude}{Average longitude.}
#' \item{area}{Surface area in square kilometer.}
#' }
#' @source \url{https://opendata.socrata.com/dataset/Country-List-ISO-3166-Codes-Latitude-Longitude/mnkm-8ram}
#'         
#'         \url{https://www.kaggle.com/fernandol/countries-of-the-world}
#' @seealso \code{\link{gapminder}} for a description of the dataset
#' @examples
#' if (require("dplyr")) {
#' gapminder %>%
#'   filter(year == 2007, continent == "Asia") %>%
#'   left_join(country_geo, by = "country")
#' }
"country_geo"