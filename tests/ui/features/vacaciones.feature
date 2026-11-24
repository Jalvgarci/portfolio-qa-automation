Feature: Solicitud y aprobación de vacaciones

  Scenario: Un empleado nuevo solicita vacaciones y el administrador las aprueba
    Given inicio sesión como administrador
    When doy de alta un empleado nuevo con usuario de acceso
    Then el empleado figura dado de alta
    When asigno días de vacaciones al empleado nuevo
    Then los días de vacaciones figuran asignados
    When cierro sesión
    Then inicio sesión como empleado
    When el empleado solicita vacaciones
    Then la solicitud figura pendiente de aprobación
    When cierro sesión
    Given inicio sesión como administrador
    When apruebo la solicitud de vacaciones del empleado
    And cierro sesión
    And inicio sesión como empleado
    Then la solicitud figura aprobada
    When cierro sesión
