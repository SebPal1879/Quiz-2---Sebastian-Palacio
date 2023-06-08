# Llamado de librerías y webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service = Service("driver/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.maximize_window()
time.sleep(1)

driver.get("https://www.carulla.com") #Acceso a la página de Carulla
time.sleep(1) #Tiempos de espera para evitar acciones sin que haya cargado la página

hamburguesa = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div/div/button') #Acceso al menú hamburguesa
time.sleep(1)
hamburguesa.click()
time.sleep(1)

vidaSana = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div/div/div[1]/ul/li[6]/div[2]/p') #Acceso a "Vida sana"
time.sleep(1)
vidaSana.click()
time.sleep(1)

gliuten = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div/div/section/div/div[2]/div[2]/div[1]/a[1]/strong') #Acceso a "Libre de gluten"
time.sleep(1)
gliuten.click()
time.sleep(6)

ciudad = driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/span') #Acceso a "Ciudad (Medellín)"
time.sleep(4)
ciudad.click()
time.sleep(4)

aa = driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/div/div[3]/div') #Selección a "Ciudad (Medellín)"
time.sleep(1)
aa.click()
time.sleep(5)



almacen = driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div/div/div[2]/div[4]/div[3]/div[2]/div/div/div/div[1]') #Acceso a "Almacén" (selecciona el primero)
time.sleep(1)
almacen.click()
time.sleep(5)


confirmar = driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div/div/div[2]/div[4]/div[3]/div[2]/div/div[2]/div/div[1]') #Confirma el almacén
time.sleep(1)
confirmar.click()
time.sleep(8) #Puede demorarse cargando




acepta = driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div/div/div[2]/div[6]/button') #Acepta
time.sleep(1)
acepta.click()
time.sleep(6) 

checkbox = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[3]/div/div[15]/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div/div[3]/div[2]/div/div/div[5]/div/div/input') #Filtro
checkbox.click()
time.sleep(6) 

# /html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div['+str(i+1)+']/section/a/article/div[3]/div[2]/div/div/div/div[4]
# /html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[2]/section/a/article/div[3]/div[2]/div/div/div/div[4]
# /html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[3]/section/a/article/div[3]/div[2]/div/div/div/div[4]

# /html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div['+str(i+1)+']/section/a/article/div[3]/div[2]/div/div/div/div[2]

# /html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div['+str(i+1)+']/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span
# /html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[3]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span


for i in range(4):
 print("Buenas tardunas")
 nombre = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[' + str(i+1) + ']/section/a/article/div[3]/div[2]/div/div/div/div[2]').text
 precio = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[' + str(i+1) + ']/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span').text
 print("")
 print("")
 print("Nombre: " + nombre)
 print("Precio es: $" + precio)
 time.sleep(2)

producto = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[3]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span') #Acepta
time.sleep(1)
producto.click()
time.sleep(6) 

placeholder =  driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[6]/div/section/div/div[2]/div/div')
placeholder.click()


body = driver.find_element(By.TAG_NAME, "body") #Obtener el cuerpo de la página
body.send_keys(Keys.END)# Desplazarse hasta el fondo de la página
time.sleep(5)


yt = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div/div[2]/section/div/div[3]/div/div[2]/div/div[1]/div[2]/a[4]')
yt.click()
time.sleep(10)

driver.quit()
