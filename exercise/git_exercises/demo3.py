#将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中
import redis
import uuid

def create_activation_code(count=200):
    codes = set()
    [codes.add(str(uuid.uuid1())) for i in range(count)]
    return codes

if __name__ == "__main__":
    codes = create_activation_code(count=200)

    r = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)
    [r.sadd("activation_code", code) for code in codes]