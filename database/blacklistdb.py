#    This file is part of NiceGrill.

#    NiceGrill is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    NiceGrill is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with NiceGrill.  If not, see <https://www.gnu.org/licenses/>.

from database.mongo import cli

cli = cli["NiceGrill"]["Blacklist"]

async def add_blacklist(id):
    return cli.insert_one({"Blacklist": id})

async def check_blacklist(id):
    return (False if not cli.find_one({"Blacklist": id})
        else True)

async def delete_blacklist(id):
    return cli.delete_one({"Blacklist": id})