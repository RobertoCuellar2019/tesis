 function[u2]=propTFR(u1,lambda,z,e)
%%%funcion de transferencia de propagación de fresnel
 % L es la longitud horizontal
 % 
 % u1 es el plano de entrada (transparencia por la amplitud de la onda plana)
 % L - lado del cuadrado de entrada y de observación
 % lambda - longitud de onda
 % z - distancia de propagación
 % u2 - plano de observación 
 M=e;
 %M=768;%%pixeles horizontales
 %N=768;%%pixeles verticales
 N=e;
 LX=(M*19e-6);
 LY=(N*19e-6);
 
 dx=LX/M; %intervalo de muestreo en el eje x
 dy=LX/N; % intervalo de muesteo sobre el eje y
 k=2*pi/lambda; %número de onda

 fx=-1/(2*dx):1/LX:1/(2*dx)-1/LX; %coordenadas del espacio de frecuencias en direccion fx
 fy=-1/(2*dy):1/LY:1/(2*dx)-1/LY; %coordenadas del espacio de frecuencias en direccion fy
 [FX,FY]=meshgrid(fx,fy); %%%arreglo bidimensional frecuencial

 H=(exp(-j*pi*lambda*z*(FX.^2+FY.^2))); %Funcion de transferencia
 H=fftshift(H); %Se organizan los datos de la función de transferencia para que se puedan tratar con la fft2
 U1=fft2(fftshift(u1)); %se organiza el plano de entrada y se lleva al espacio frecuencial
 U2=H.*U1; %Multiplicación en el espacio de frecuencias
 u2=ifftshift(ifft2(U2)); %Se halla el campo con ifft2 y se centra la señal
 end