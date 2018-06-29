import unittest
import unittest
import sys
sys.path.append("..")

from models.test_bed_options import TestBedOptions
from models.consumer_kafka import ConsumerKafka
from models.avro_schema_helper import AvroSchemaHelper

import logging
logging.basicConfig(level=logging.INFO)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        options ={
          "auto_register_schemas":False,
          #"kafka_host": 'driver-testbed.eu:3501',
          #"schema_registry": 'http://driver-testbed.eu:3502',
          "kafka_host": '127.0.0.1:3501',
          "schema_registry": 'http://localhost:3502',
          "fetch_all_versions": False,
          "client_id": 'ConsumerErik',
          "consume": None}

        test_bed_options = TestBedOptions(options)

        schema_sr_key = '{"type":"record","name":"EDXLDistribution","namespace":"eu.driver.model.edxl","fields":[{"name":"distributionID","type":"string","doc":"The unique identifier of this distribution message."},{"name":"senderID","type":"string","doc":"The unique identifier of the sender."},{"name":"dateTimeSent","type":"long","doc":"The date and time the distribution message was sent as the number of milliseconds from the unix epoch, 1 January 1970 00:00:00.000 UTC.","logicalType":"timestamp-millis"},{"name":"dateTimeExpires","type":"long","doc":"The date and time the distribution message should expire as the number of milliseconds from the unix epoch, 1 January 1970 00:00:00.000 UTC.","logicalType":"timestamp-millis"},{"name":"distributionStatus","type":{"type":"enum","name":"DistributionStatus","symbols":["Actual","Exercise","System","Test","Unknown","NoAppropriateDefault"]},"doc":"The action-ability of the message."},{"name":"distributionKind","type":{"type":"enum","name":"DistributionKind","symbols":["Report","Update","Cancel","Request","Response","Dispatch","Ack","Error","SensorConfiguration","SensorControl","SensorStatus","SensorDetection","Unknown","NoAppropriateDefault"]},"doc":"The function of the message."}]}'
        #schema_sr_value = '{"type":"record","name":"Alert","namespace":"eu.driver.model.cap","fields":[{"name":"identifier","type":"string"},{"name":"sender","type":"string"},{"name":"sent","type":"string","doc":"TODO xs:dateTime Used pattern"},{"name":"status","type":{"type":"enum","name":"Status","symbols":["Actual","Exercise","System","Test","Draft"]}},{"name":"msgType","type":{"type":"enum","name":"MsgType","symbols":["Alert","Update","Cancel","Ack","Error"]}},{"name":"source","type":["null","string"],"default":null},{"name":"scope","type":{"type":"enum","name":"Scope","symbols":["Public","Restricted","Private"]}},{"name":"restriction","type":["null","string"],"default":null},{"name":"addresses","type":["null","string"],"default":null},{"name":"code","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"note","type":["null","string"],"default":null},{"name":"references","type":["null","string"],"default":null},{"name":"incidents","type":["null","string"],"default":null},{"name":"info","type":["null",{"type":"record","name":"Info","fields":[{"name":"language","type":["string","null"],"default":"en-US"},{"name":"category","type":[{"type":"enum","name":"Category","symbols":["Geo","Met","Safety","Security","Rescue","Fire","Health","Env","Transport","Infra","CBRNE","Other"]},{"type":"array","items":"Category"}]},{"name":"event","type":"string"},{"name":"responseType","type":["null",{"type":"enum","name":"ResponseType","symbols":["Shelter","Evacuate","Prepare","Execute","Avoid","Monitor","Assess","AllClear","None"]},{"type":"array","items":"ResponseType"}],"default":null},{"name":"urgency","type":{"type":"enum","name":"Urgency","symbols":["Immediate","Expected","Future","Past","Unknown"]}},{"name":"severity","type":{"type":"enum","name":"Severity","symbols":["Extreme","Severe","Moderate","Minor","Unknown"]}},{"name":"certainty","type":{"type":"enum","name":"Certainty","symbols":["Observed","Likely","Possible","Unlikely","Unknown"]}},{"name":"audience","type":["null","string"],"default":null},{"name":"eventCode","type":["null",{"type":"record","name":"ValueNamePair","fields":[{"name":"valueName","type":"string"},{"name":"value","type":"string"}]},{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"effective","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"onset","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"expires","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"senderName","type":["null","string"],"default":null},{"name":"headline","type":["null","string"],"default":null},{"name":"description","type":["null","string"],"default":null},{"name":"instruction","type":["null","string"],"default":null},{"name":"web","type":["null","string"],"doc":"TODO: anyURI","default":null},{"name":"contact","type":["null","string"],"default":null},{"name":"parameter","type":["null","ValueNamePair",{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"resource","type":["null",{"type":"record","name":"Resource","fields":[{"name":"resourceDesc","type":"string"},{"name":"size","type":["null","int"],"default":null},{"name":"uri","type":["null","string"],"doc":"TODO, anyURI","default":null},{"name":"deferUri","type":["null","string"],"default":null},{"name":"digest","type":["null","string"],"default":null}]},{"type":"array","items":"Resource"}],"default":null},{"name":"area","type":["null",{"type":"record","name":"Area","fields":[{"name":"areaDesc","type":"string"},{"name":"polygon","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"circle","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"geocode","type":["null","ValueNamePair",{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"altitude","type":["null","double"],"default":null},{"name":"ceiling","type":["null","double"],"default":null}]},{"type":"array","items":"Area"}],"default":null}]},{"type":"array","items":"Info"}],"default":null}]}'
        #schema_sr_value = '{"type":"record","name":"Alert","namespace":"eu.driver.model.cap","doc":"CAP Alert Message (version 1.2)","fields":[{"name":"identifier","type":"string"},{"name":"sender","type":"string"},{"name":"sent","type":"string","doc":"TODO xs:dateTime Used pattern"},{"name":"status","type":{"type":"enum","name":"Status","symbols":["Actual","Exercise","System","Test","Draft"]}},{"name":"msgType","type":{"type":"enum","name":"MsgType","symbols":["Alert","Update","Cancel","Ack","Error"]}},{"name":"source","type":["null","string"],"default":null},{"name":"scope","type":{"type":"enum","name":"Scope","symbols":["Public","Restricted","Private"]}},{"name":"restriction","type":["null","string"],"default":null},{"name":"addresses","type":["null","string"],"default":null},{"name":"code","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"note","type":["null","string"],"default":null},{"name":"references","type":["null","string"],"default":null},{"name":"incidents","type":["null","string"],"default":null},{"name":"info","type":["null",{"type":"record","name":"Info","fields":[{"name":"language","type":["string","null"],"default":"en-US"},{"name":"category","type":[{"type":"enum","name":"Category","symbols":["Geo","Met","Safety","Security","Rescue","Fire","Health","Env","Transport","Infra","CBRNE","Other"]},{"type":"array","items":"Category"}]},{"name":"event","type":"string"},{"name":"responseType","type":["null",{"type":"enum","name":"ResponseType","symbols":["Shelter","Evacuate","Prepare","Execute","Avoid","Monitor","Assess","AllClear","None"]},{"type":"array","items":"ResponseType"}],"default":null},{"name":"urgency","type":{"type":"enum","name":"Urgency","symbols":["Immediate","Expected","Future","Past","Unknown"]}},{"name":"severity","type":{"type":"enum","name":"Severity","symbols":["Extreme","Severe","Moderate","Minor","Unknown"]}},{"name":"certainty","type":{"type":"enum","name":"Certainty","symbols":["Observed","Likely","Possible","Unlikely","Unknown"]}},{"name":"audience","type":["null","string"],"default":null},{"name":"eventCode","type":["null",{"type":"record","name":"ValueNamePair","fields":[{"name":"valueName","type":"string"},{"name":"value","type":"string"}]},{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"effective","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"onset","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"expires","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"senderName","type":["null","string"],"default":null},{"name":"headline","type":["null","string"],"default":null},{"name":"description","type":["null","string"],"default":null},{"name":"instruction","type":["null","string"],"default":null},{"name":"web","type":["null","string"],"doc":"TODO: anyURI","default":null},{"name":"contact","type":["null","string"],"default":null},{"name":"parameter","type":["null","ValueNamePair",{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"resource","type":["null",{"type":"record","name":"Resource","fields":[{"name":"resourceDesc","type":"string"},{"name":"size","type":["null","int"],"default":null},{"name":"uri","type":["null","string"],"doc":"TODO, anyURI","default":null},{"name":"mimeType","type":["null","string"],"doc":"The mimetype of the resource!","default":null},{"name":"deferUri","type":["null","string"],"default":null},{"name":"digest","type":["null","string"],"default":null}]},{"type":"array","items":"Resource"}],"default":null},{"name":"area","type":["null",{"type":"record","name":"Area","fields":[{"name":"areaDesc","type":"string"},{"name":"polygon","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"circle","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"geocode","type":["null","ValueNamePair",{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"altitude","type":["null","double"],"default":null},{"name":"ceiling","type":["null","double"],"default":null}]},{"type":"array","items":"Area"}],"default":null}]},{"type":"array","items":"Info"}],"default":null}]}'
        #schema_sr_value ='\{\"name\":\"eu.driver.model.cap.Alert\",\"namespace\":\"eu.driver.model.cap\",\"doc\":\"CAPAlertMessage(version1.2)\",\"type\":\"record\",\"fields\":[\{\"name\":\"identifier\",\"type\":\"string\"\\},\{\"name\":\"sender\",\"type\":\"string\"\\},\{\"name\":\"sent\",\"type\":\"string\",\"doc\":\"TODOxs:dateTimeUsedpattern\"\\},\{\"name\":\"status\",\"type\":\{\"name\":\"Status\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"enum\",\"symbols\":[\"Actual\",\"Exercise\",\"System\",\"Test\",\"Draft\"]\\}\\},\{\"name\":\"msgType\",\"type\":\{\"name\":\"MsgType\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"enum\",\"symbols\":[\"Alert\",\"Update\",\"Cancel\",\"Ack\",\"Error\"]\\}\\},\{\"name\":\"source\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"scope\",\"type\":\{\"name\":\"Scope\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"enum\",\"symbols\":[\"Public\",\"Restricted\",\"Private\"]\\}\\},\{\"name\":\"restriction\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"addresses\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"code\",\"type\":[\"null\",\"string\",\{\"type\":\"array\",\"items\":\"string\"\\}],\"default\":null\\},\{\"name\":\"note\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"references\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"incidents\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"info\",\"type\":[\"null\",\{\"name\":\"Info\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"record\",\"fields\":[\{\"name\":\"language\",\"default\":\"en-US\",\"type\":[\"string\",\"null\"]\\},\{\"name\":\"category\",\"type\":[\{\"name\":\"Category\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"enum\",\"symbols\":[\"Geo\",\"Met\",\"Safety\",\"Security\",\"Rescue\",\"Fire\",\"Health\",\"Env\",\"Transport\",\"Infra\",\"CBRNE\",\"Other\"]\\},\{\"type\":\"array\",\"items\":\"eu.driver.model.cap.Category\"\\}]\\},\{\"name\":\"event\",\"type\":\"string\"\\},\{\"name\":\"responseType\",\"type\":[\"null\",\{\"name\":\"ResponseType\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"enum\",\"symbols\":[\"Shelter\",\"Evacuate\",\"Prepare\",\"Execute\",\"Avoid\",\"Monitor\",\"Assess\",\"AllClear\",\"None\"]\\},\{\"type\":\"array\",\"items\":\"eu.driver.model.cap.ResponseType\"\\}],\"default\":null\\},\{\"name\":\"urgency\",\"type\":\{\"name\":\"Urgency\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"enum\",\"symbols\":[\"Immediate\",\"Expected\",\"Future\",\"Past\",\"Unknown\"]\\}\\},\{\"name\":\"severity\",\"type\":\{\"name\":\"Severity\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"enum\",\"symbols\":[\"Extreme\",\"Severe\",\"Moderate\",\"Minor\",\"Unknown\"]\\}\\},\{\"name\":\"certainty\",\"type\":\{\"name\":\"Certainty\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"enum\",\"symbols\":[\"Observed\",\"Likely\",\"Possible\",\"Unlikely\",\"Unknown\"]\\}\\},\{\"name\":\"audience\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"eventCode\",\"type\":[\"null\",\{\"name\":\"ValueNamePair\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"record\",\"fields\":[\{\"name\":\"valueName\",\"type\":\"string\"\\},\{\"name\":\"value\",\"type\":\"string\"\\}]\\},\{\"type\":\"array\",\"items\":\"eu.driver.model.cap.ValueNamePair\"\\}],\"default\":null\\},\{\"name\":\"effective\",\"doc\":\"TODO:datetime\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"onset\",\"doc\":\"TODO:datetime\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"expires\",\"doc\":\"TODO:datetime\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"senderName\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"headline\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"description\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"instruction\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"web\",\"doc\":\"TODO:anyURI\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"contact\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"parameter\",\"type\":[\"null\",\"eu.driver.model.cap.ValueNamePair\",\{\"type\":\"array\",\"items\":\"eu.driver.model.cap.ValueNamePair\"\\}],\"default\":null\\},\{\"name\":\"resource\",\"type\":[\"null\",\{\"name\":\"Resource\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"record\",\"fields\":[\{\"name\":\"resourceDesc\",\"type\":\"string\"\\},\{\"name\":\"size\",\"type\":[\"null\",\"int\"],\"default\":null\\},\{\"name\":\"uri\",\"doc\":\"TODO,anyURI\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"deferUri\",\"type\":[\"null\",\"string\"],\"default\":null\\},\{\"name\":\"digest\",\"type\":[\"null\",\"string\"],\"default\":null\\}]\\},\{\"type\":\"array\",\"items\":\"eu.driver.model.cap.Resource\"\\}],\"default\":null\\},\{\"name\":\"area\",\"type\":[\"null\",\{\"name\":\"Area\",\"namespace\":\"eu.driver.model.cap\",\"type\":\"record\",\"fields\":[\{\"name\":\"areaDesc\",\"type\":\"string\"\\},\{\"name\":\"polygon\",\"type\":[\"null\",\"string\",\{\"type\":\"array\",\"items\":\"string\"\\}],\"default\":null\\},\{\"name\":\"circle\",\"type\":[\"null\",\"string\",\{\"type\":\"array\",\"items\":\"string\"\\}],\"default\":null\\},\{\"name\":\"geocode\",\"type\":[\"null\",\"eu.driver.model.cap.ValueNamePair\",\{\"type\":\"array\",\"items\":\"eu.driver.model.cap.ValueNamePair\"\\}],\"default\":null\\},\{\"name\":\"altitude\",\"type\":[\"null\",\"double\"],\"default\":null\\},\{\"name\":\"ceiling\",\"type\":[\"null\",\"double\"],\"default\":null\\}]\\},\{\"type\":\"array\",\"items\":\"eu.driver.model.cap.Area\"\\}],\"default\":null\\}]\\},\{\"type\":\"array\",\"items\":\"eu.driver.model.cap.Info\"\\}],\"default\":null\\}]\\}'

        schema_sr_value = b'{"type":"record","name":"Alert","namespace":"eu.driver.model.cap","doc":"CAP Alert Message (version 1.2)","fields":[{"name":"identifier","type":"string"},{"name":"sender","type":"string"},{"name":"sent","type":"string","doc":"TODO xs:dateTime Used pattern"},{"name":"status","type":{"type":"enum","name":"Status","symbols":["Actual","Exercise","System","Test","Draft"]}},{"name":"msgType","type":{"type":"enum","name":"MsgType","symbols":["Alert","Update","Cancel","Ack","Error"]}},{"name":"source","type":["null","string"],"default":null},{"name":"scope","type":{"type":"enum","name":"Scope","symbols":["Public","Restricted","Private"]}},{"name":"restriction","type":["null","string"],"default":null},{"name":"addresses","type":["null","string"],"default":null},{"name":"code","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"note","type":["null","string"],"default":null},{"name":"references","type":["null","string"],"default":null},{"name":"incidents","type":["null","string"],"default":null},{"name":"info","type":["null",{"type":"record","name":"Info","fields":[{"name":"language","type":["string","null"],"default":"en-US"},{"name":"category","type":[{"type":"enum","name":"Category","symbols":["Geo","Met","Safety","Security","Rescue","Fire","Health","Env","Transport","Infra","CBRNE","Other"]},{"type":"array","items":"Category"}]},{"name":"event","type":"string"},{"name":"responseType","type":["null",{"type":"enum","name":"ResponseType","symbols":["Shelter","Evacuate","Prepare","Execute","Avoid","Monitor","Assess","AllClear","None"]},{"type":"array","items":"ResponseType"}],"default":null},{"name":"urgency","type":{"type":"enum","name":"Urgency","symbols":["Immediate","Expected","Future","Past","Unknown"]}},{"name":"severity","type":{"type":"enum","name":"Severity","symbols":["Extreme","Severe","Moderate","Minor","Unknown"]}},{"name":"certainty","type":{"type":"enum","name":"Certainty","symbols":["Observed","Likely","Possible","Unlikely","Unknown"]}},{"name":"audience","type":["null","string"],"default":null},{"name":"eventCode","type":["null",{"type":"record","name":"ValueNamePair","fields":[{"name":"valueName","type":"string"},{"name":"value","type":"string"}]},{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"effective","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"onset","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"expires","type":["null","string"],"doc":"TODO: datetime","default":null},{"name":"senderName","type":["null","string"],"default":null},{"name":"headline","type":["null","string"],"default":null},{"name":"description","type":["null","string"],"default":null},{"name":"instruction","type":["null","string"],"default":null},{"name":"web","type":["null","string"],"doc":"TODO: anyURI","default":null},{"name":"contact","type":["null","string"],"default":null},{"name":"parameter","type":["null","ValueNamePair",{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"resource","type":["null",{"type":"record","name":"Resource","fields":[{"name":"resourceDesc","type":"string"},{"name":"size","type":["null","int"],"default":null},{"name":"uri","type":["null","string"],"doc":"TODO, anyURI","default":null},{"name":"mimeType","type":["null","string"],"doc":"The mimetype of the resource!","default":null},{"name":"deferUri","type":["null","string"],"default":null},{"name":"digest","type":["null","string"],"default":null}]},{"type":"array","items":"Resource"}],"default":null},{"name":"area","type":["null",{"type":"record","name":"Area","fields":[{"name":"areaDesc","type":"string"},{"name":"polygon","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"circle","type":["null","string",{"type":"array","items":"string"}],"default":null},{"name":"geocode","type":["null","ValueNamePair",{"type":"array","items":"ValueNamePair"}],"default":null},{"name":"altitude","type":["null","double"],"default":null},{"name":"ceiling","type":["null","double"],"default":null}]},{"type":"array","items":"Area"}],"default":null}]},{"type":"array","items":"Info"}],"default":null}]}'
        topic = b"standard_cap"
        client_id = test_bed_options.client_id

        avro_schema_helper_value = AvroSchemaHelper(schema_sr_value, topic)
        avro_schema_helper_key = AvroSchemaHelper(schema_sr_key, topic)

        on_message_handler = lambda x: logging.info(x)

        consumer_kafka = ConsumerKafka(topic, test_bed_options, on_message_handler, avro_schema_helper_key, avro_schema_helper_value)

        consumer_kafka.listen_messages()


        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
