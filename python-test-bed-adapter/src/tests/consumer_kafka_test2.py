import unittest
import sys
sys.path.append("..")
import os
from test_bed_options import TestBedOptions
from kafka_manager import KafkaManager
from avro_schema_helper import AvroSchemaHelper

import logging
logging.basicConfig(level=logging.INFO)

class MyTestCase(unittest.TestCase):

    @unittest.skip("This test can use an outdated version of your schema")
    def test_something(self):
        options ={
          "auto_register_schemas": False,
          #"kafka_host": 'driver-testbed.eu:3501',
          #"schema_registry": 'http://driver-testbed.eu:3502',
          "kafka_host": '127.0.0.1:3501',
          "schema_registry": 'http://localhost:3502',
          "fetch_all_versions": False,
          "from_off_set":True,
          "client_id": 'ConsumerErik',
          "consume": None}

        test_bed_options = TestBedOptions(options)
        #schema_sr_value = '{"name":"Item","namespace":"eu.driver.model.sim.entity","doc":"CommonSimulationSpaceItem,representingavisualentityinsidethesimulationworld.*Copyright(C)2017-2018XVRSimulationB.V.,Delft,TheNetherlands,MartijnHendriks<hendriks@xvrsim.com>.ThisfileispartofDRIVER+WP923Test-bedinfrastructureproject.ThisfileislicensedundertheMITlicense:https://github.com/DRIVER-EU/avro-schemas/blob/master/LICENSE*","type":"record","fields":[{"name":"guid","doc":"globallyuniqueidentifierforthisentity","type":"string"},{"name":"name","doc":"nameofthisentity","type":"string"},{"name":"owner","doc":"identifierofthesimulatorcurrentlyresponsibleforthisentity","type":"string"},{"name":"location","doc":"locationofthisitem","type":{"name":"Location","namespace":"eu.driver.model.sim.geo","doc":"WGS84-basedstandardrepresentationofalocationonearth","type":"record","fields":[{"name":"latitude","doc":"latitudeindegrees(-90,90]-0isequator","type":"long"},{"name":"longitude","doc":"longitudeindegrees(-180,180]-0isline[geographicnorth-Greenwich-geographicsouth]","type":"long"},{"name":"altitude","doc":"altitudeinmeters-0issurfaceofWGS84-basedellipsoid","type":"long"}]}},{"name":"orientation","doc":"orientationofthisitem","type":{"name":"Orientation","namespace":"eu.driver.model.sim.geo","doc":"WGS84/Aviation-basedrepresentationofanorientationonearth-Right-handeditem-specificreferencesystem,withinbase-settingheading/yaw-axispointingdown(tothecentreoftheearth),pitch-axispointingtotheright,roll/bank-axispointingforward","type":"record","fields":[{"name":"yaw","doc":"yaworheadingindegrees[0,360)-0ispointingtowardsgeographicnorth-yawof90isEAST,yawof270isWEST","type":"long"},{"name":"pitch","doc":"pitchindegrees(-90,90]-0isperpendiculartoline[originofitem-centreofWGS84-basedellipsoid]-pitchof+45is45degreespointingupwards,-45is45degreespointingdownwards","type":"long"},{"name":"roll","doc":"rollorbankindegrees(-180,180]-0isperpendiculartoline[originofitem-centreofWGS84-basedellipsoid]-bankof+45is45degreesrolltotheright,-45is45degreesrolltotheleft","type":"long"}]}},{"name":"velocity","doc":"movementvectoroftheitem,includingthemagnitude","type":{"name":"Velocity","namespace":"eu.driver.model.sim.geo","doc":"WGS84/Aviation-basedrepresentationofavelocityvector.Right-handeditem-specificreferencesystem,withinbase-settingheading/yaw-axispointingdown(tothecentreoftheearth),pitch-axispointingtotheright,roll/bank-axispointingforward","type":"record","fields":[{"name":"yaw","doc":"yaworheadingindegrees[0,360)-0ispointingtowardsgeographicnorth-yawof90isEAST,yawof270isWEST","type":"long"},{"name":"pitch","doc":"pitchindegrees(-90,90]-0isperpendiculartoline[originofitem-centreofWGS84-basedellipsoid]-pitchof+45is45degreespointingupwards,-45is45degreespointingdownwards","type":"long"},{"name":"magnitude","doc":"velocityinmeterpersecond[0,inf)-0isstandingstillrelativetotheearth","type":"long"}]}},{"name":"visibleForParticipant","doc":"indicationwhetherornotthisitemisvisibleforallparticipants","type":"boolean"},{"name":"movable","doc":"indicationwhetherornotthisitemismovableinthesimulationworld","type":"boolean"},{"name":"itemType","doc":"concretetypeofthisitem-canbeoftypeObjectType,PersonTypeorVehicleType","type":["null",{"name":"ObjectType","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemisanobject","type":"record","fields":[{"name":"subType","doc":"subtypeofobjectsthatthisitemis","type":{"name":"ObjectSubType","type":"enum","symbols":["PROP","TOOL"]}}]},{"name":"PersonType","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemisaperson","type":"record","fields":[{"name":"gender","doc":"genderoftheperson","type":{"name":"PersonSubType","type":"enum","symbols":["MALE","FEMALE","UNKNOWN"]}}]},{"name":"VehicleType","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemisavehicle","type":"record","fields":[{"name":"subType","doc":"subtypeofvehiclesthatthisitemis","type":{"name":"VehicleSubType","type":"enum","symbols":["CAR","VAN","TRUCK","BOAT","PLANE","HELICOPTER","MOTORCYCLE"]}}]}],"default":null},{"name":"scenarioLabel","doc":"scenariotypeofthisitem-canbeoftypeEnvironmentLabel,IncidentLabelorRescueLabel","type":["null",{"name":"EnvironmentLabel","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemislabeledasenvironment","type":"record","fields":[{"name":"subLabel","doc":"sublabelofenvironmentthatthisitemhas","type":{"name":"EnvironmentSubLabel","type":"enum","symbols":["FOLIAGE","ROAD"]}}]},{"name":"IncidentLabel","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemislabeledasincident","type":"record","fields":[{"name":"subLabel","doc":"sublabelofincidentthatthisitemhas","type":{"name":"IncidentSubLabel","type":"enum","symbols":["FIRE","CRASH"]}}]},{"name":"RescueLabel","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemislabeledasrescue","type":"record","fields":[{"name":"subLabel","doc":"sublabelofrescuethatthisitemhas","type":{"name":"RescueSubLabel","type":"enum","symbols":["POLICE","MEDICAL","FIRE","SECURITY","MILITARY"]}}]}],"default":null},{"name":"userTags","doc":"listofalltagstheuserprovidedassociatedwiththisitem","type":["null",{"type":"array","items":"string"}],"default":null},{"name":"physicalConnections","doc":"listofphysicalconnectionentitiesreferences(representedbytheirGUIDs)thisitemhas","type":["null",{"type":"array","items":"string"}],"default":null},{"name":"group","doc":"referencetothegroupconnectionentity(representedbyitsGUID)thisitemispartof","type":["null","string"],"default":null},{"name":"formation","doc":"referencetotheformationconnectionentity(representedbyitsGUID)thisitemispartof","type":["null","string"],"default":null},{"name":"unit","doc":"referencetotheunitconnectionentity(representedbyitsGUID)thisitemispartof","type":["null","string"],"default":null}]}'

        dirname = os.path.dirname(__file__)
        filename = os.path.join(sys.path[0], 'data/schemas/simulation/simulation_entity_item-value.avsc')
        schema_sr_value = open(filename).read()

        schema_sr_key = '{"name":"Item","namespace":"eu.driver.model.sim.entity","doc":"CommonSimulationSpaceItem,representingavisualentityinsidethesimulationworld.*Copyright(C)2017-2018XVRSimulationB.V.,Delft,TheNetherlands,MartijnHendriks<hendriks@xvrsim.com>.ThisfileispartofDRIVER+WP923Test-bedinfrastructureproject.ThisfileislicensedundertheMITlicense:https://github.com/DRIVER-EU/avro-schemas/blob/master/LICENSE*","type":"record","fields":[{"name":"guid","doc":"globallyuniqueidentifierforthisentity","type":"string"},{"name":"name","doc":"nameofthisentity","type":"string"},{"name":"owner","doc":"identifierofthesimulatorcurrentlyresponsibleforthisentity","type":"string"},{"name":"location","doc":"locationofthisitem","type":{"name":"Location","namespace":"eu.driver.model.sim.geo","doc":"WGS84-basedstandardrepresentationofalocationonearth","type":"record","fields":[{"name":"latitude","doc":"latitudeindegrees(-90,90]-0isequator","type":"double"},{"name":"longitude","doc":"longitudeindegrees(-180,180]-0isline[geographicnorth-Greenwich-geographicsouth]","type":"double"},{"name":"altitude","doc":"altitudeinmeters-0issurfaceofWGS84-basedellipsoid","type":"double"}]}},{"name":"orientation","doc":"orientationofthisitem","type":{"name":"Orientation","namespace":"eu.driver.model.sim.geo","doc":"WGS84/Aviation-basedrepresentationofanorientationonearth-Right-handeditem-specificreferencesystem,withinbase-settingheading/yaw-axispointingdown(tothecentreoftheearth),pitch-axispointingtotheright,roll/bank-axispointingforward","type":"record","fields":[{"name":"yaw","doc":"yaworheadingindegrees[0,360)-0ispointingtowardsgeographicnorth-yawof90isEAST,yawof270isWEST","type":"double"},{"name":"pitch","doc":"pitchindegrees(-90,90]-0isperpendiculartoline[originofitem-centreofWGS84-basedellipsoid]-pitchof+45is45degreespointingupwards,-45is45degreespointingdownwards","type":"double"},{"name":"roll","doc":"rollorbankindegrees(-180,180]-0isperpendiculartoline[originofitem-centreofWGS84-basedellipsoid]-bankof+45is45degreesrolltotheright,-45is45degreesrolltotheleft","type":"double"}]}},{"name":"velocity","doc":"movementvectoroftheitem,includingthemagnitude","type":{"name":"Velocity","namespace":"eu.driver.model.sim.geo","doc":"WGS84/Aviation-basedrepresentationofavelocityvector.Right-handeditem-specificreferencesystem,withinbase-settingheading/yaw-axispointingdown(tothecentreoftheearth),pitch-axispointingtotheright,roll/bank-axispointingforward","type":"record","fields":[{"name":"yaw","doc":"yaworheadingindegrees[0,360)-0ispointingtowardsgeographicnorth-yawof90isEAST,yawof270isWEST","type":"double"},{"name":"pitch","doc":"pitchindegrees(-90,90]-0isperpendiculartoline[originofitem-centreofWGS84-basedellipsoid]-pitchof+45is45degreespointingupwards,-45is45degreespointingdownwards","type":"double"},{"name":"magnitude","doc":"velocityinmeterpersecond[0,inf)-0isstandingstillrelativetotheearth","type":"double"}]}},{"name":"visibleForParticipant","doc":"indicationwhetherornotthisitemisvisibleforallparticipants","type":"boolean"},{"name":"movable","doc":"indicationwhetherornotthisitemismovableinthesimulationworld","type":"boolean"},{"name":"itemType","doc":"concretetypeofthisitem-canbeoftypeObjectType,PersonTypeorVehicleType","type":["null",{"name":"ObjectType","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemisanobject","type":"record","fields":[{"name":"subType","doc":"subtypeofobjectsthatthisitemis","type":{"name":"ObjectSubType","type":"enum","symbols":["PROP","TOOL"]}}]},{"name":"PersonType","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemisaperson","type":"record","fields":[{"name":"gender","doc":"genderoftheperson","type":{"name":"PersonSubType","type":"enum","symbols":["MALE","FEMALE","UNKNOWN"]}}]},{"name":"VehicleType","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemisavehicle","type":"record","fields":[{"name":"subType","doc":"subtypeofvehiclesthatthisitemis","type":{"name":"VehicleSubType","type":"enum","symbols":["CAR","VAN","TRUCK","BOAT","PLANE","HELICOPTER","MOTORCYCLE"]}}]}],"default":null},{"name":"scenarioLabel","doc":"scenariotypeofthisitem-canbeoftypeEnvironmentLabel,IncidentLabelorRescueLabel","type":["null",{"name":"EnvironmentLabel","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemislabeledasenvironment","type":"record","fields":[{"name":"subLabel","doc":"sublabelofenvironmentthatthisitemhas","type":{"name":"EnvironmentSubLabel","type":"enum","symbols":["FOLIAGE","ROAD"]}}]},{"name":"IncidentLabel","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemislabeledasincident","type":"record","fields":[{"name":"subLabel","doc":"sublabelofincidentthatthisitemhas","type":{"name":"IncidentSubLabel","type":"enum","symbols":["FIRE","CRASH"]}}]},{"name":"RescueLabel","namespace":"eu.driver.model.sim.entity.item","doc":"informationiftheitemislabeledasrescue","type":"record","fields":[{"name":"subLabel","doc":"sublabelofrescuethatthisitemhas","type":{"name":"RescueSubLabel","type":"enum","symbols":["POLICE","MEDICAL","FIRE","SECURITY","MILITARY"]}}]}],"default":null},{"name":"userTags","doc":"listofalltagstheuserprovidedassociatedwiththisitem","type":["null",{"type":"array","items":"string"}],"default":null},{"name":"physicalConnections","doc":"listofphysicalconnectionentitiesreferences(representedbytheirGUIDs)thisitemhas","type":["null",{"type":"array","items":"string"}],"default":null},{"name":"group","doc":"referencetothegroupconnectionentity(representedbyitsGUID)thisitemispartof","type":["null","string"],"default":null},{"name":"formation","doc":"referencetotheformationconnectionentity(representedbyitsGUID)thisitemispartof","type":["null","string"],"default":null},{"name":"unit","doc":"referencetotheunitconnectionentity(representedbyitsGUID)thisitemispartof","type":["null","string"],"default":null}]}'
        topic = b"simulation-entity-item"
        client_id = test_bed_options.client_id

        avro_helper_value = AvroSchemaHelper(schema_sr_value, topic)
        avro_helper_key = AvroSchemaHelper(schema_sr_key, topic)

        on_message_handler = lambda x: logging.info(x)

        consumer_kafka = KafkaManager(topic, test_bed_options.kafka_host, test_bed_options.from_off_set, client_id, avro_helper_key,
                                      avro_helper_value, on_message_handler)

        consumer_kafka.listen_messages()


        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()