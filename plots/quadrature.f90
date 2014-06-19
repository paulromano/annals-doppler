program hermite

  integer, parameter :: MAX_ITERATIONS = 100       ! Max # of iterations for finding roots
  real,    parameter :: EPS = 1.0e-6             ! Covergence criteria for roots
  real,    parameter :: PIM4 = 0.7511255444649425 ! 1/pi^0.25

  integer :: n           ! order of Hermite polynomial
  integer :: m,it,i,j
  real    :: p1,p2,p3,pp,z,z1

!---begin execution

  do n = 2, 30
    z = sqrt(real(2*n+1)) - 1.85575*(2.0*n + 1.0)**(-0.16667)
  
    z1 = 0.0
    it = 1
    do while(abs(z-z1) > eps)
      p1 = PIM4
      p2 = 0.0

      do j = 1,n
        p3 = p2
        p2 = p1
        p1 = z*sqrt(2.0/j)*p2 - sqrt(real(j-1)/real(j))*p3
      end do

      ! Now p1 is the desired Hermite poly. Next compute the derivative, pp,
      ! by using the relation given in Num. Rec. (4.5.21) and p2, the poly of
      ! one lower order.

      pp = sqrt(2.0*n)*p2
      z1 = z
      z  = z1 - p1/pp

      it = it + 1
!!$      if(it > MAX_ITERATIONS) then
!!$        write(*,*) "Exceeded max iterations."
!!$        stop
!!$      end if
    end do

    print *, n, z
  end do

end program hermite
