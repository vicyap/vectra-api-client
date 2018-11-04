"""Detect API v1 Responses"""
import attr


@attr.s
class DetectionsGET(object):
    count = attr.ib(default=None, converter=int)
    next = attr.ib(default=None, converter=str)
    previous = attr.ib(default=None, converter=str)
    results = attr.ib(default=None)

    @classmethod
    def from_dict(cls, d):
        return cls(
            count=d.get('count'),
            next=d.get('next'),
            previous=d.get('previous'),
            results=[DetectionsGET.Detection.from_dict(x) for x in d.get('results')]
        )


    @results.validator
    def check(self, attribute, value):
        if not isinstance(value, list):
            raise ValueError('results must be a list')
        for v in value:
            if not isinstance(v, DetectionsResponse.Detection):
                raise ValueError('results must be a list of Detection objects')

    @attr.s
    class Detection(object):
        id = attr.ib(default=None, converter=int)
        type_vname = attr.ib(default=None, converter=str)
        category = attr.ib(default=None, converter=str)
        source = attr.ib(default=None, converter=str)
        state = attr.ib(default=None, converter=str)
        description = attr.ib(default=None, converter=str)
        t_score = attr.ib(default=None, converter=int)
        c_score = attr.ib(default=None, converter=int)
        first_timestamp = attr.ib(default=None, converter=str)  # datetime?
        last_timestamp = attr.ib(default=None, converter=str)  # datetime?
        detection_detail_set = attr.ib(default=None)
        sensor_luid = attr.ib(default=None, converter=str)
        app_id = attr.ib(default=None)
        host = attr.ib(default=None, converter=str)
        url = attr.ib(default=None, converter=str)

        @classmethod
        def from_dict(cls, d):
            return cls(
                id=d.get('id'),
                type_vname=d.get('type_vname'),
                category=d.get('category'),
                source=d.get('source'),
                state=d.get('state'),
                description=d.get('description'),
                t_score=d.get('t_score'),
                c_score=d.get('c_score'),
                first_timestamp=d.get('first_timestamp'),
                last_timestamp=d.get('last_timestamp'),
                detection_detail_set=
                    DetectionsGET.DetectionDetailSet.from_dict(
                        d.get('detection_detail_set')[0]),
                sensor_luid=d.get('sensor_luid'),
                app_id=d.get('app_id'),
                host=d.get('host'),
                url=d.get('url'),
            )

        @detection_detail_set.validator
        def check(self, attribute, value):
            if not isinstance(value, DetectionsGET.DetectionDetailSet):
                raise ValueError('detection_detail_set must be a DetectionDetailSet object')

    @attr.s
    class DetectionDetailSet(object):
        id = attr.ib(default=None)
        description = attr.ib(default=None)
        destination = attr.ib(default=None)
        count = attr.ib(default=None)
        count_pos = attr.ib(default=None)
        dst_port = attr.ib(default=None)
        dst_geo = attr.ib(default=None)
        proto = attr.ib(default=None)
        first_timestamp = attr.ib(default=None)  # datetime
        last_timestamp = attr.ib(default=None)  # datetime
        total_bytes_sent = attr.ib(default=None)
        total_bytes_rcvd = attr.ib(default=None)
        url = attr.ib(default=None)

        @classmethod
        def from_dict(cls, d):
            return cls(
                id=d.get('id'),
                description=d.get('description'),
                destination=d.get('destination'),
                count=d.get('count'),
                count_pos=d.get('count_pos'),
                dst_port=d.get('dst_port'),
                dst_geo=d.get('dst_geo'),
                proto=d.get('proto'),
                first_timestamp=d.get('first_timestamp'),
                last_timestamp=d.get('last_timestamp'),
                total_bytes_sent=d.get('total_bytes_sent'),
                total_bytes_rcvd=d.get('total_bytes_rcvd'),
                url=d.get('url'),
            )


class HealthGET(object):
    pass


class HealthSubnetsGET(object):
    pass


class HealthHeadendGET(object):
    class Subnets(object):
        pass
    class Traffic(object):
        pass


class HealthSubnetCountsGET(object):
    pass


class HealthTrafficGET(object):
    pass
